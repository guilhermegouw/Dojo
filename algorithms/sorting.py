import unittest
import time


def bubble_sort(input_list):
    did_swap = True
    until_idx = len(input_list)
    while did_swap:
        did_swap = False
        for i in range(1, until_idx):
            if input_list[i] < input_list[i-1]:
                input_list[i-1], input_list[i] = input_list[i], input_list[i-1]
                did_swap = True
        until_idx -= 1
    return input_list


"""
bubble sort
0 | 1 | 2 | 3 | 4 
-----------------
5 | 3 | 1 | 6 | 2 => idx 0 > idx 1 
3 | 5 | 1 | 6 | 2 => idx 1 > idx 2
3 | 1 | 5 | 6 | 2 => idx 2 < idx 3
3 | 1 | 5 | 6 | 2 => idx 3 > idx 4 - Arrived in the last idx
3 | 1 | 5 | 2 | 6 => idx 0 > idx 1
1 | 3 | 5 | 6 | 2 => idx 1 < idx 2
1 | 3 | 5 | 6 | 2 => idx 2 < idx 3
1 | 3 | 5 | 6 | 2 => idx 3 > idx 4 - Arrived in the last idx
1 | 3 | 5 | 2 | 6 => idx 0 < idx 1
1 | 3 | 5 | 2 | 6 => idx 1 < idx 2
1 | 3 | 5 | 2 | 6 => idx 2 > idx 3
1 | 3 | 2 | 5 | 6 => idx 3 < idx 4 - Arrived in the last idx
1 | 3 | 2 | 5 | 6 => idx 0 < idx 1
1 | 3 | 2 | 5 | 6 => idx 1 > idx 2
1 | 2 | 3 | 5 | 6 => idx 2 < idx 3
1 | 2 | 3 | 5 | 6 => idx 3 < idx 4 - Arrived in the last idx
1 | 2 | 3 | 5 | 6 => idx 0 < idx 1
1 | 2 | 3 | 5 | 6 => idx 1 < idx 2
1 | 2 | 3 | 5 | 6 => idx 2 < idx 3
1 | 2 | 3 | 5 | 6 => idx 3 < idx 4 - Arrived in the last idx, with no swaps! List is sorted.
"""

def my_sort(input_list):
    sorted_list = []
    for i in range(len(input_list)):
        sorted_list.append(input_list[0])
        for elem in input_list:
            if elem < sorted_list[i]:
                sorted_list[i] = elem
        input_list.remove(sorted_list[i])
    return sorted_list

"""
my sort
0 | 1 | 2 | 3 | 4 
-----------------
5 | 3 | 1 | 6 | 2 => sorted_list = [5]
5 | 3 | 1 | 6 | 2 => sorted_list = [3]
5 | 3 | 1 | 6 | 2 => sorted_list = [1]
5 | 3 | 1 | 6 | 2 => sorted_list = [1]
5 | 3 | 1 | 6 | 2 => sorted_list = [1]
5 | 3 | 6 | 2 => sorted_list = [1, 5]
5 | 3 | 6 | 2 => sorted_list = [1, 3]
5 | 3 | 6 | 2 => sorted_list = [1, 3]
5 | 3 | 6 | 2 => sorted_list = [1, 2]
5 | 3 | 6 => sorted_list = [1, 2, 5]
5 | 3 | 6 => sorted_list = [1, 2, 3]
5 | 3 | 6 => sorted_list = [1, 2, 3]
5 | 6 => sorted_list = [1, 2, 3, 5]
5 | 6 => sorted_list = [1, 2, 3, 5]
6 => sorted_list = [1, 2, 3, 5, 6]
"""

def insertion_sort(unsorted_list):
    for i, entry in enumerate(unsorted_list):
        current = i
        while current > 0 and unsorted_list[current] < unsorted_list[current -1]:
            unsorted_list[current], unsorted_list[current -1] = unsorted_list[current -1], unsorted_list[current]
            current -= 1
    return unsorted_list

"""
Insertion sort

0 | 1 | 2 | 3 | 4 
-----------------
5 | 3 | 1 | 2 | 4 => idx 0 > idx 1
3 | 5 | 1 | 2 | 4 => idx 1 > idx 2
3 | 1 | 5 | 2 | 4 => idx 0 > idx 1
1 | 3 | 5 | 2 | 4 => idx 2 > idx 3
1 | 3 | 2 | 5 | 4 => idx 1 > idx 2
1 | 2 | 3 | 5 | 4 => idx 3 > idx 4
1 | 2 | 3 | 4 | 5 => idx 3 > idx 4
"""
def selection_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        min_idx = i
        for j in range(i, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_idx]:
                min_idx = j
        unsorted_list[i], unsorted_list[min_idx] = unsorted_list[min_idx], unsorted_list[i]
    return unsorted_list

"""
Selection sort

0 | 1 | 2 | 3 | 4 
-----------------
5 | 3 | 1 | 2 | 4 => smallest idx = 2 swap 0 - 2
1 | 3 | 5 | 2 | 4 => smallest idx = 3 swap 1 - 3
1 | 2 | 3 | 5 | 4 => smallest idx = 3 swap 3 - 2
1 | 2 | 3 | 5 | 4 => smallest idx = 4 swap 3 - 4
1 | 2 | 3 | 4 | 5 => sorted
"""


if __name__=='__main__':
    unsorted_list = [i for i in range(10000)]
    unsorted_list = unsorted_list[::-1]
    start = time.time()
    bubble_sort(unsorted_list)
    bubble_sort_time = time.time() - start
    print(f'Bubble sort: {bubble_sort_time}')
    start = time.time()
    my_sort(unsorted_list)
    my_sort_time = time.time() - start
    print(f'My sort: {my_sort_time}')
    start = time.time()
    insertion_sort(unsorted_list)
    insertion_sort_time = time.time() - start
    print(f'Insertion sort: {insertion_sort_time}')
    start = time.time()
    selection_sort(unsorted_list)
    selection_sort_time = time.time() - start
    print(f'Selection sort: {selection_sort_time}')
    result = [bubble_sort_time, my_sort_time, insertion_sort_time, selection_sort_time]
    print(sorted(result))