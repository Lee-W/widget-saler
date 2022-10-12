from dataclasses import dataclass

from widget_saler.product import Product
from widget_saler.rule import DeliveryCostChargeRule, SepcialOfferRule


@dataclass
class BasketConfig:
    products: list[Product]
    delivery_cost_rules: list[DeliveryCostChargeRule]
    special_offer_rules: list[SepcialOfferRule]

    # TODO: sort delivery_cost_rules


class Basket:
    def __init__(self, basket_config: BasketConfig) -> None:
        self.basket_config = basket_config

    def add(self, product_code: str) -> None:
        pass

    @property
    def total(self) -> float:
        pass
