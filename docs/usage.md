## Initialize Basket Config

In `BasicConfig`, we can customize `products`, `delivery_cost_rules` and `special_offer_rules`. The input format is shown as follows.


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
```

### Column definitions

#### product

The configuration for defining products

* `name`: the name of the product
* `code`: the id to identify this product. it'll be used in special offer rules
* `price`: the price of the product

#### special offer rule

The configuration for defining an offer for a particular product
When the amount of product reaches `product_amount`, the user can get a discount equal to `price * amount * discount_ratio`. For example, “buy one red widget, get the second half price” is 25% off.

* `product_code`: the product code of the product we'll apply this offer rule on
* `product_amount`: the amount of product purchased needed to get this offer
* `discount_ratio`: the discount ratio of this offer. Note that this ratio applies to the whole group

For example, if we have the following setup without delivery cost rules.

```python
basket_config = BasketConfig(
    products=[{"name": "Red Widget", "code": "R01", "price": 5}],
    special_offer_rules=[{"product_code": "R01", "product_amount": 2, "discount_ratio": 0.25}],
)
```

1. When we buy the first "R01", we'll need to pay 5 dollars without discount as we've not yet achieved `product_amount = 2`.
2. When we buy the second "R01" , we can get our first discount which is 5 (price) * 2 (amount) * 0.25 (discount) = 2.5. Thus, we only need to pay 10 - 2.5 = 7.5 for this order (not including delivery cost).
3. When we buy the third "R01", we won't be able to trigger another offer. Thus, we'll need to pay 7.5 + 5 = 12.5.
4. When we buy the fourth "R01", we can get our second discount 2.5. The total we'll need to pay becomes 5 * 4 - 2.5 - 2.5 = 15.

#### delivery cost rule

The rule deciding the delivery cost of each purchase
Each rule decides only the highest price of this delivery interval, and the previous rules will determine the lowest price of this interval. If there's no previous rule, then the lowest price of that interval will be 0.
Delivery cost is calculated after the offer discount.

* `lower_than_threshold`: the highest price of this delivery cost interval (the previous rules decide the lowest price)
* `delivery_cost`: the delivery cost of this interval

We sort given delivery cost rules in acceding order on the column `lower_than_threshold`.

Given the following delivery cost rules

```python
[
    {"lower_than_threshold": 90, "delivery_cost": 2.95},
    {"lower_than_threshold": 50, "delivery_cost": 4.95}
]
```

they'll be sorted as

```python
[
    {"lower_than_threshold": 50, "delivery_cost": 4.95},
    {"lower_than_threshold": 90, "delivery_cost": 2.95}
]
```

which implies the following delivery cost rules.


| interval | price |
| --- | --- |
| 0 | 0 |
| (0, 50) | 4.95 |
| [50, 90) | 2.95 |
| [90, +∞)  | 0 |

If the order total is 0, the delivery cost should also be 0. Therefore, 0 is not included in the first interval.

## Add new products to the basket

In a basket, we only store the count of each product. You can pass a single product code or a list of product codes to the `add` method.

```python
from widget_saler.basket import Basket


basket = Basket()  # use the default config
basket.add("R01")  # now we have {"R01": 1}
basket.add(["R01", "G01"])  # now we have {"R01": 2, "G01": 1}
```

## Calculate the price of the products in the basket

widger_saler supports calculating the `pure_toal`, `discount`, `discounted_pure_total` `delivery_cost`,  and `total`,  of the products in the basket.

* `pure_total`: sum up all the prices of products without considering the discount or delivery cost
* `discount`: the discount after applying `special_offer_rules`
* `discounted_pure_total`: `pure_total` - `discount`
* `delivery_cost`: check which interval is `discounted_pure_total` in and get the corresponding delivery cost
* `total`: `discounted_pure_total` + `delivery_cost`


Following the previous example, we have `{"R01": 2, "G01": 1}` in our basket. Then, we can get the following values.

```python
from widget_saler.basket import Basket


basket = Basket()  # use the default config
basket.add("R01")  # now we have {"R01": 1}
basket.add(["R01", "G01"])  # now we have {"R01": 2, "G01": 1}


basket.pure_total
# 90.85000000000001

basket.discount
# 16.475

basket.discounted_pure_total
# 74.375

basket.delivery_cost
# 2.95

basket.total
# 77.325
```
