"""
The Luhn formula is a widely used system for validating identification numbers.
Using the original number, double the value every other digit. Then add the 
values of the individual digits together (if a doubled value now has two digits,
add the digits individually). If the total is divisible by 10, the number is valid.

Write a program that takes an identification number of any length and validates
that the number is valid per the Luhn formula. The program must process each
character before reading the next one.

Example:

Input: 176248
total = 0
processing: 1
total = 1
processing: 7 -> 7 * 2 = 14 -> 1 + 4 = 5
total = 6
processing: 6
total = 12
processing: 2 -> 2 * 2 = 4 -> 4
total = 16
processing: 4
total = 20
processing: 8 -> 8 * 2 = 16 -> 1 + 6 = 7
total = 27

check digit = 30 - 27 = 3

Input: 123456
total = 0
processing: 1
total = 1
processing: 2 -> 2 * 2 = 4 -> 4
total = 5
processing: 3
total = 8
processing: 4 -> 4 * 2 = 8
total = 16
processing: 5
total = 21
processing: 6 -> 6 * 2 = 12 -> 1 + 2 = 3
total = 24

check digit = 30 - 24 = 6


"""


def should_double(id_num: str, current_index: int) -> bool:
    """Check if the current index should be doubled

    Args:
        id_num (str): The identification number
        current_index (int): The current index

    Returns:
        bool: Even-length id_num double the digits with odd indexes,
        Odd-length id_num double the digits with even indexes
    """
    return (current_index + len(id_num)) % 2 == 0


def get_doubled_values(num_to_double: str) -> int:
    """Get the number to double, then double it,
    and return the sum of the digits of the doubled number.

    Args:
        num_to_double (str): The number to double

    Returns:
        int: The sum of the digits of the doubled number
    """
    doubled_num = int(num_to_double) * 2
    if doubled_num >= 10:
        doubled_num = sum(int(digit) for digit in str(doubled_num))
    return doubled_num


def luhn_checksum_validation(id_num: str) -> bool:
    """Validate the Luhn checksum

    Args:
        id_num (str): The identification number

    Returns:
        bool: True if the Luhn checksum is valid
    """
    total = 0
    for i in range(len(id_num)):
        if should_double(id_num, i):
            total += get_doubled_values(id_num[i])
        else:
            total += int(id_num[i])
    return total % 10 == 0
