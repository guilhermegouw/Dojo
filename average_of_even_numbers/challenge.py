"""
The mean average of even numbers will be defined as the sum of all the even
numbers in a list, divided by the total number of even numbers in the list.
"""
import time


def average_of_even_numbers(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    try:
        return sum(even_numbers) / len(even_numbers)
    except ZeroDivisionError:
        return 0


def book_average_of_even_numbers(numbers):
    evens_sum = 0
    count_of_evens = 0
    for number in numbers:
        if number % 2 == 0:
            evens_sum += number
            count_of_evens += 1
    try:
        return evens_sum / count_of_evens
    except ZeroDivisionError:
        return 0


if __name__ == "__main__":
    numbers = [number for number in range(1, 1_000_000)]
    start = time.time()
    average_of_even_numbers(numbers)
    my_duration = time.time() - start
    start = time.time()
    book_average_of_even_numbers(numbers)
    book_duration = time.time() - start
    print(my_duration, book_duration)
