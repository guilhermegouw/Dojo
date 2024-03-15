import time


def bubble_sort(input):
    did_swap = True
    until_idx = len(input)
    while did_swap:
        did_swap = False
        for i in range(1, until_idx):
            if input[i] < input[i - 1]:
                input[i - 1], input[i] = input[i], input[i - 1]
                did_swap = True
        until_idx -= 1
    return input


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
1 | 2 | 3 | 5 | 6 => idx 3 < idx 4 - Arrived in the last idx, with no swaps!
List is sorted.
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


def insertion_sort(unsorted):
    for i, entry in enumerate(unsorted):
        current = i
        while current > 0 and unsorted[current] < unsorted[current - 1]:
            unsorted[current], unsorted[current - 1] = (
                unsorted[current - 1],
                unsorted[current],
            )
            current -= 1
    return unsorted



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


def insertion_sort_book(unsorted):
    for i in range(1, len(unsorted)):
        temp = unsorted[i]
        position = i - 1
        while position >= 0:
            if unsorted[position] > temp:
                unsorted[position + 1] = unsorted[position]
                position -= 1
            else:
                break
        unsorted[position + 1] = temp
    return unsorted


"""
Insertion sort book

0 | 1 | 2 | 3 | 4
-----------------
4 | 2 | 7 | 1 | 3 => temp(idx 1) = 2: 
                     idx 0 (4) > temp (2)
                     => idx 1 = idx 0 (4)
                     => idx 0 = temp
2 | 4 | 7 | 1 | 3 => temp(idx 2) = 7: 
                     idx 1 (4) < temp (7)
                     => idx 2 (7) = idx 1 (4)
                     idx 0 (2) < temp (7)
                     => idx 1 = idx 0 (2)
                     => idx 0 = temp
1 | 2 | 4 | 7 | 3 => temp(idx 3) = 1 
                     idx 2 (4) > temp (1) 
                     => idx 3 = idx 2 (4)
                     idx 1 (2) > temp (1) 
                     => idx 2 = idx 1 (2)
                     idx 0 > temp 
                     idx 0 = temp
1 | 2 | 3 | 4 | 7 => temp(idx 4) = 3 
                     idx 3 (7) > temp (3) 
                     => idx 4 = idx 3 (7)
                     idx 2 (4) > temp 
                     => idx 3 = idx 2 (4)
                     idx 1 (2) > temp
"""


def selection_sort(unsorted):
    for i in range(len(unsorted)):
        min_idx = i
        for j in range(i, len(unsorted)):
            if unsorted[j] < unsorted[min_idx]:
                min_idx = j
        if min_idx != i:
            unsorted[i], unsorted[min_idx] = unsorted[min_idx], unsorted[i]
    return unsorted


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


if __name__ == "__main__":
    unsorted_list = [i for i in range(10000)]
    unsorted_list = unsorted_list[::-1]
    start = time.time()
    bubble_sort(unsorted_list)
    bubble_sort_time = time.time() - start
    print(f"Bubble sort: {bubble_sort_time}")
    start = time.time()
    my_sort(unsorted_list)
    my_sort_time = time.time() - start
    print(f"My sort: {my_sort_time}")
    start = time.time()
    insertion_sort(unsorted_list)
    insertion_time = time.time() - start
    print(f"Insertion sort: {insertion_time}")
    start = time.time()
    selection_sort(unsorted_list)
    selection_time = time.time() - start
    print(f"Selection sort: {selection_time}")
    start = time.time()
    insertion_sort_book(unsorted_list)
    insertion_sort_book_time = time.time() - start
    print(f"Insertion sort book: {selection_time}")
    result = [
        bubble_sort_time,
        my_sort_time,
        insertion_time,
        selection_time,
        insertion_sort_book_time,
    ]
    print(sorted(result))
