from typing import TypedDict


class SepcialOfferRule(TypedDict):
    product_code: str
    amount: int
    discount: float


class DeliveryCostChargeRule(TypedDict):
    lower_than_threshold: float
    delivery_cost: float
