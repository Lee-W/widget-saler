from collections import Counter

from widget_saler.basket_config import BasketConfig
from widget_saler.defaults import default_basket_config
from widget_saler.product import Product


class Basket:
    def __init__(self, basket_config: BasketConfig = default_basket_config) -> None:
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
        if not self.item_counter:
            return 0

        return self.discounted_pure_total + self.delivery_cost

    @property
    def discounted_pure_total(self) -> float:
        return self.pure_total - self.discount

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
        if not self.item_counter:
            return 0

        discount_sum: float = 0
        for offer in self.basket_config.special_offer_rules:
            product_code = offer["product_code"]
            item_amount = self.item_counter[product_code]
            if not item_amount:
                continue

            offer_product_amount = offer["product_amount"]
            # calculate how many groups of product can hve discount
            discount_group_count = item_amount // offer_product_amount
            discount_price = (
                discount_group_count
                * offer_product_amount
                * self.product_code_mapping[product_code]["price"]
                * offer["discount_ratio"]
            )

            discount_sum += discount_price

        return discount_sum

    @property
    def delivery_cost(self) -> float:
        if not self.item_counter:
            return 0

        discounted_pure_total = self.discounted_pure_total
        for delivery_cost_rule in self.basket_config.delivery_cost_rules:
            if discounted_pure_total < delivery_cost_rule["lower_than_threshold"]:
                return delivery_cost_rule["delivery_cost"]

        return 0
