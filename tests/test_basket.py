import pytest

from widget_saler.basket import Basket, BasketConfig


@pytest.fixture
def basket_config() -> BasketConfig:
    return BasketConfig(
        products=[
            {
                "name": "Red Widget",
                "code": "R01",
                "price": 32.95,
            },
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


@pytest.mark.parametrize(
    "product_codes, expected_total",
    (
        (("B01", "G01"), 37.85),
        (("R01", "R01"), 54.37),
        (("R01", "G01"), 60.85),
        (("B01", "B01", "R01", "R01", "R01"), 98.25),
        ((), 0),
    ),
)
def test_basket_total(
    product_codes: list[str], expected_total: float, basket_config: BasketConfig
):
    basket = Basket(basket_config)
    for product_code in product_codes:
        basket.add(product_code)

    assert basket.total == expected_total
