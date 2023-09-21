"""
Function receive a list and return True if at least one value is duplicated.  
"""
import time


def has_duplicate_quadratic(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if i != j and input_list[i] == input_list[j]:
                return True
    return False

def has_duplicated_with_list(input_list):
    elements_list = []
    for value in input_list:
        if value not in elements_list:
            elements_list.append(value)
        else:
            return True
    return False

def has_duplicate_dict(input_list):
    elements_dict = {}
    for value in input_list:
        if value not in elements_dict:
            elements_dict[value] = 1
        else:
            return True
    return False


if __name__=='__main__':
    test_list = [i for i in range(10_000)]
    start = time.time()
    has_duplicate_quadratic(test_list)
    finished = time.time()
    print(f'Quadratic: {finished - start}')
    start = time.time()
    has_duplicated_with_list(test_list)
    finished = time.time()
    print(f'With list: {finished - start}')
    start = time.time()
    has_duplicate_dict(test_list)
    finished = time.time()
    print(f'With dict: {finished - start}')