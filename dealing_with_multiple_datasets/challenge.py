"""
Now, what happens if instead of computing the product of every two numbers from
a single array, we instead compute the product of every number from one array
by every number of a second array?
For example, if we had the array, [1, 2, 3] and the array, [10, 100, 1000],
we'd compute the products as:

[10, 100, 1000, 20, 200, 2000, 30, 300, 3000]
"""

from itertools import product


def products_between_arrays(array1, array2):
    products = []
    for item in array1:
        for item2 in array2:
            products.append(item * item2)
    return products


def products_between_arrays2(array1, array2):
    products = [x * y for x, y in list(product(array1, array2))]
    return products
