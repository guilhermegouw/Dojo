def intersection(first_array, second_array):
    """Returns the intersection of two arrays.

    Args:
        first_array (list): The first array.
        second_array (list): The second array.

    Returns:
        list: The intersection of the two arrays.
    """
    return list(set(first_array).intersection(set(second_array)))


def force_intersection(first_array, second_array):
    return [elem for elem in set(first_array) if elem in set(second_array)]


def force_intersection2(first_array, second_array):
    intersection = []
    for elem in first_array:
        if elem in second_array and elem not in intersection:
            intersection.append(elem)
    return intersection


if __name__ == "__main__":
    import time

    test_list_1 = [i for i in range(10_000)]
    test_list_2 = [i for i in range(5_000, 15_000)]
    start = time.time()
    intersection(test_list_1, test_list_2)
    finished = time.time()
    print(f"Intersection: {finished - start}")
    start = time.time()
    force_intersection(test_list_1, test_list_2)
    finished = time.time()
    print(f"Force intersection: {finished - start}")
    start = time.time()
    force_intersection2(test_list_1, test_list_2)
    finished = time.time()
    print(f"Force intersection 2: {finished - start}")
    assert (
        intersection(test_list_1, test_list_2)
        == force_intersection(test_list_1, test_list_2)
        == force_intersection2(test_list_1, test_list_2)
    )
