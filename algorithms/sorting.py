import unittest


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


class TestBubbleSort(unittest.TestCase):

    def test_one_element_list(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_two_elements_list(self):
        self.assertEqual(bubble_sort([2, 1]), [1, 2])

    def test_three_elements_list(self):
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])

    def test_four_elements_list(self):
        self.assertEqual(bubble_sort([0, 3, 2, 1]), [0, 1, 2, 3])

    def test_five_elements_list(self):
        self.assertEqual(bubble_sort([4, 2, 7, 1, 3]), [1, 2, 3, 4, 7])

if __name__=='__main__':
    unittest.main()



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
