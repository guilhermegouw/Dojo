def intersection(first_array, second_array):
    """Returns the intersection of two arrays.

    Args:
        first_array (list): The first array.
        second_array (list): The second array.

    Returns:
        list: The intersection of the two arrays.
    """
    return list(set(first_array) & set(second_array))
