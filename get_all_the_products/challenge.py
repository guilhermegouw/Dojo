"""
Algorithm that accepts an array of numbers and returns the product of every
combination of two numbers.

For example, if we passed in the array, [1, 2, 3, 4, 5], the function returns:

[2, 3, 4, 5, 6, 8, 10, 12, 15, 20]

This is because we first multiply the 1 by the 2, 3, 4, and 5.
Then we multiply the 2 by the 3, 4, and 5.
Next, we multiply the 3 by the 4 and the 5.
And finally, we multiply the 4 by the 5.

Note something interesting:
when we multiply, say, the 2 by the other numbers, we only have to multiply it
by the numbers that are to the right of it.
We don't have to go back and multiply 2 by the 1,
because that was already covered back when we multiplied by the 1 by the 2.
So, each number only needs to be multiplied by the remaining numbers to the
right of it.
"""


def get_all_the_products(numbers):
    result = []
    for i in range(len(numbers)):
        multiplier = numbers[i]
        for num in numbers[i + 1:]:
            result.append(multiplier * num)
    return result
