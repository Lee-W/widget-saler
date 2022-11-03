import pytest

from widget_saler.basket import Basket


@pytest.mark.parametrize(
    "product_codes, expected_total",
    (
        (("B01", "G01"), 37.85),
        (("R01", "R01"), 54.37),
        (("R01", "G01"), 60.85),
        (("B01", "B01", "R01", "R01", "R01"), 98.27),
        ((), 0),
    ),
)
def test_basket_total(product_codes: list[str], expected_total: float):
    basket = Basket()
    for product_code in product_codes:
        basket.add(product_code)

    assert basket.total == expected_total
    # assert basket.total == pytest.approx(expected_total, 0.001)
