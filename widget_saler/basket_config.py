from dataclasses import dataclass

from widget_saler.product import Product
from widget_saler.rule import DeliveryCostChargeRule, SpecialOfferRule


@dataclass
class BasketConfig:
    products: list[Product]
    delivery_cost_rules: list[DeliveryCostChargeRule]
    special_offer_rules: list[SpecialOfferRule]

    def __post_init__(self) -> None:
        # ensure shipping_fee can check the threshold in correct order
        self.delivery_cost_rules.sort(key=lambda rule: rule["lower_than_threshold"])
