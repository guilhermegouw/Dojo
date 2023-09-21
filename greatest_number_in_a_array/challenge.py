"""
Function receives an array of numbers and return the greatest of them. 
"""


def get_greatest_number(input_list):
    greatest_num = input_list[0]
    for num in input_list:
        if num > greatest_num:
            greatest_num = num
    return greatest_num
