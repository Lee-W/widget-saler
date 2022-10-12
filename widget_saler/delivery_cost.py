from typing import TypedDict


class DeliveryCostChargeRule(TypedDict):
    lower_than_threshold: float
    delivery_cost: float
