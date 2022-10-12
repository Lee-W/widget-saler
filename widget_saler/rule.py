from typing import TypedDict


class SpecialOfferRule(TypedDict):
    product_code: str
    product_amount: int

    # The total discount_ratio of this group offer group
    # e.g., Buy 1 get 1 implys 50% off for the 2 products.
    #       This value should be set to 0.5
    discount_ratio: float


class DeliveryCostChargeRule(TypedDict):
    lower_than_threshold: float
    delivery_cost: float
