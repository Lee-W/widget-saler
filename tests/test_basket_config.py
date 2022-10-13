from widget_saler.basket_config import BasketConfig
from widget_saler.defaults import default_basket_config


def test_load_json() -> None:
    # the content is the same as default config
    new_basket_config = BasketConfig.load_json("tests/data/sample_config.json")

    assert new_basket_config.products == default_basket_config.products
    assert (
        new_basket_config.special_offer_rules
        == default_basket_config.special_offer_rules
    )
    assert (
        new_basket_config.delivery_cost_rules
        == default_basket_config.delivery_cost_rules
    )
