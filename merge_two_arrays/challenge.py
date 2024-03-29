"""
It merges two sorted arrays together to create a new sorted array
containing all the values from both arrays:

Example:

array_1 = [1, 2, 3]
array_2 = [4, 5, 6]

result = [1, 2, 3, 4, 5, 6]
"""


def merge(array_1, array_2):
    return sorted(array_1 + array_2)


def merge_2(array_1, array_2):
    result = []
    i = 0
    j = 0
    while i < len(array_1) and j < len(array_2):
        if array_1[i] < array_2[j]:
            result.append(array_1[i])
            i += 1
        else:
            result.append(array_2[j])
            j += 1
    result.extend(array_1[i:])
    result.extend(array_2[j:])
    return result


"""
arr1 = [1, 10] => len = 2
arr2 = [2, 3, 4, 5, 6, 7, 8, 9, 11] => len = 9
result = []


i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] (1) < arr2[j] (2):        (1) < (2) => result.append(1)
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1
return result

"""
