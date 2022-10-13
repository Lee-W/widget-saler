# Changelog

## 0.2.0 (2022-10-13)

### Feat

- **defaults**: add default basket config
- **basket**: handle list of product codes and single product code in add method
- **basket**: implment add method and total, shipping_fee, discount, pure_toal property
- **basket**: add BasketConfig for configuring products, rules
- **widget_saler**: add typed_dict for basket configurations (i.e. delivery_cost, offer, product)
- **widget_saler/basket**: add Basket class skeleton and minimum test cases to it

### Fix

- **rule**: add comment to describe how speical offer rules work and fix typo

### Refactor

- **basket**: rename discounted_total as discounted_pure_total to avoid confusion
- **basket**: rename shipping_fee as delivery_cost for consistency
- **basket**: add discounted_total property to avoid naming confusion
- **rule**: rename discount as discount_ratio in special offer rule
- **rule**: rename amount as product_amount
- merge delivery_cost and offer as rule

## 0.1.0 (2022-10-12)

### Feat

- initial project through Lee-W/cookiecutter-python-template
