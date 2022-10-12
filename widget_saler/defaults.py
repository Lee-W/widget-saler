from widget_saler.basket_config import BasketConfig

default_basket_config = BasketConfig(
    products=[
        {"name": "Red Widget", "code": "R01", "price": 32.95},
        {"name": "Green Widget", "code": "G01", "price": 24.95},
        {"name": "Blue Widget", "code": "B01", "price": 7.95},
    ],
    delivery_cost_rules=[
        {"lower_than_threshold": 50, "delivery_cost": 4.95},
        {"lower_than_threshold": 90, "delivery_cost": 2.95},
    ],
    special_offer_rules=[
        {"product_code": "R01", "product_amount": 2, "discount_ratio": 0.25}
    ],
)
