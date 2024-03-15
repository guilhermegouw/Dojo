import pytest

from sorting import bubble_sort, my_sort, selection_sort, insertion_sort_book


@pytest.mark.parametrize(
    "input_list, result",
    [
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([0, 3, 2, 1], [0, 1, 2, 3]),
        ([4, 2, 7, 1, 3], [1, 2, 3, 4, 7]),
    ],
)
def test_bubble_sort(input_list, result):
    assert bubble_sort(input_list) == result


@pytest.mark.parametrize(
    "input_list, result",
    [
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([0, 3, 2, 1], [0, 1, 2, 3]),
        ([4, 2, 7, 1, 3], [1, 2, 3, 4, 7]),
    ],
)
def test_my_sort(input_list, result):
    assert my_sort(input_list) == result

@pytest.mark.parametrize(
    "input_list, result",
    [
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([0, 3, 2, 1], [0, 1, 2, 3]),
        ([4, 2, 7, 1, 3], [1, 2, 3, 4, 7]),
    ],
)
def test_selection_sort(input_list, result):
    assert selection_sort(input_list) == result


@pytest.mark.parametrize(
    "input_list, result",
    [
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([0, 3, 2, 1], [0, 1, 2, 3]),
        ([4, 2, 7, 1, 3], [1, 2, 3, 4, 7]),
    ],
)
def test_insertion_sort_book(input_list, result):
    assert insertion_sort_book(input_list) == result
