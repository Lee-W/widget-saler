## Assumption
1. The user will use it as a Python package instead of a command line tool or an API backend.
2. The order of the products added to the basket is irreverent.
3. The delivery and special cost rules won't conflict.
4. The user won't input invalid input (e.g., price < 0)
5. There won't be a huge among of products added and the cost related `property` won't be called frequently. Thus, using `property` to calculate `total` could be reasonable. Otherwise, they should be turned into functions.
6. The user won't mess up with the internal values of a `Basket` instance, which might break the consistency of `basket_config.products` and `product_code_mapping`.

## Future Improvement
1. For improving assumption 2, if the order is reverent, we could use a list to store it.
2. To improve assumptions 3 and 4, we could implement a validation mechanism to check whether they conflict with each other.
3. To improve assumption 5, we could use functions to replace those `property`. We could run the calculation in a distributed system for even more significant data.
4. For improving assumption 6, we could calculate only `product_code_mapping` and drop `products` when initializing.
5. Support easier configuration ways. e.g., load from json, yaml, toml files.
6. Float rounding
