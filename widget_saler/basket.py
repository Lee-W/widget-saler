from collections import Counter
from dataclasses import dataclass

from widget_saler.product import Product
from widget_saler.rule import DeliveryCostChargeRule, SepcialOfferRule


@dataclass
class BasketConfig:
    products: list[Product]
    delivery_cost_rules: list[DeliveryCostChargeRule]
    special_offer_rules: list[SepcialOfferRule]

    def __post_init__(self) -> None:
        # ensure shipping_fee can check the threshold in correct order
        self.delivery_cost_rules.sort(key=lambda rule: rule["lower_than_threshold"])


class Basket:
    def __init__(self, basket_config: BasketConfig) -> None:
        self.basket_config = basket_config
        self.product_code_mapping: dict[str, Product] = {
            product["code"]: product for product in self.basket_config.products
        }

        self.item_counter: Counter[str] = Counter()

    def add(self, product_codes: str | list[str]) -> None:
        if isinstance(product_codes, str):
            product_codes = [product_codes]
        self.item_counter.update(product_codes)

    @property
    def total(self) -> float:
        if not len(self.item_counter):
            return 0

        return self.pure_total - self.discount + self.shipping_fee

    @property
    def pure_total(self) -> float:
        return sum(
            [
                self.product_code_mapping[product_code]["price"] * count
                for product_code, count in self.item_counter.items()
            ]
        )

    @property
    def discount(self) -> float:
        if not len(self.item_counter):
            return 0

        discount_sum: float = 0
        for offer in self.basket_config.special_offer_rules:
            product_code = offer["product_code"]
            product_amount = offer["product_amount"]
            item_amount = self.item_counter[product_code]
            if not item_amount:
                continue

            discount_group_count = item_amount // product_amount
            discount_price = (
                discount_group_count
                * product_amount
                * offer["discount_ratio"]
                * self.product_code_mapping[product_code]["price"]
            )

            discount_sum += discount_price

        return discount_sum

    @property
    def shipping_fee(self) -> float:
        if not len(self.item_counter):
            return 0

        pure_total = self.pure_total - self.discount
        for delivery_cost_rule in self.basket_config.delivery_cost_rules:
            if pure_total < delivery_cost_rule["lower_than_threshold"]:
                return delivery_cost_rule["delivery_cost"]

        return 0
