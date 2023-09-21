from random import randint
import time


class Searches:
    def linear_search(self, array, target):
        for idx, item in enumerate(array):
            if item == target:
                return idx
        return 'Not found'
    
    def linear_search_ordered_array(self, array, target):
        for idx, item in enumerate(array):
            if item == target:
                return idx
            elif item > target:
                return 'Not found'
        return 'Not found'
    
    def binary_search(self, array, target):
        first = 1
        last = len(array) - 1
        
        while first <= last:
            mid = (last + first)// 2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                last = mid -1
            elif array[mid] < target:
                first = mid + 1
        return 'Not found'


if __name__=='__main__':
    search = Searches()
    my_list = [i for i in range(1, 100000)]
    start = time.time()
    print(f'Binary Search - Index: {search.binary_search(my_list, 89999)}\nStart {start}\nFinish: {time.time()}\n it took {time.time() - start} ms')
    start = time.time()
    print(f'Linear Search - Index: {search.linear_search(my_list, 89999)}\nStart {start}\nFinish: {time.time()}\n it took {time.time() - start} ms')
    start = time.time()
    print(f'Linear Ordered Search - Index: {search.linear_search_ordered_array(my_list, 89999)}\nStart {start}\nFinish: {time.time()}\n it took {time.time() - start} ms')
