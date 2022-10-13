[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square)](https://conventionalcommits.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Github Actions](https://github.com/Lee-W/widget-saler/actions/workflows/python-check.yaml/badge.svg)](https://github.com/Lee-W/widget-saler/actions/workflows/python-check.yaml)

# Widget Saler

Widget sale system that can add customized product catalogues, delivery charge rules, and offers and calculate the total cost of an order

## Getting Started

### Prerequisites
* [Python 3.10](https://www.python.org/downloads/)

### Installation

This project is not published to [PyPI](https://pypi.org/) but [Test PyPI](https://test.pypi.org/) instead. Thus, to install this package, we'll have to add `--index-url https://test.pypi.org/simple/` before running `pip install`.

```sh
pip install --index-url https://test.pypi.org/simple/ widget_saler
```

This package can be found on Test PyPI [here](https://test.pypi.org/project/widget-saler/).

### Simple Example

```python
from widget_saler.basket import Basket
from widget_saler.basket_config import BasketConfig

# create a basket config with customized products, delivery cost rules, and special offer rules
basket_config = BasketConfig(
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

# initial basket instance with customized config
basket = Basket(basket_config)

# add a product to basket
# now we have {"R01": 1} in our basket
basket.add("R01")

# add a list of products into basket
# now we have {"R01": 3, "G01": 1} in our basket
basket.add(["R01", "R01", "G01"])

# calculate the total price
# the total would be 107.32500000000002
basket.total
```

See [Usage](usage.md) for detailed instructions

Check [Assumptions and Future Improvements](assumption_and_future_improvement.md) to know the limitation and what could be improved in this project.

## Contributing
See [Contributing](contributing.md)

## Authors
Wei Lee <weilee.rx@gmail.com>

Created from [Lee-W/cookiecutter-python-template](https://github.com/Lee-W/cookiecutter-python-template/tree/1.3.0) version 1.3.0
