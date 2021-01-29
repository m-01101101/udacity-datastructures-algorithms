"""
Implementation of quick sort
"""
from typing import List


def _pivot_idx(items, begin_index, end_index):
    left_idx = begin_index
    pivot_idx = end_index
    pivot_value = items[pivot_idx]

    while pivot_idx != left_idx:
        # because we are sorting inplace,
        # we iterate though the items to the left our our pivot
        # when an item is larger than the pivot_value;
        #     we will change the pivot_index
        #     rather than increment our position through the sub_list
        # we're done when pivot_index == left_items

        item = items[left_idx]
        if item <= pivot_value:
            left_idx += 1
            continue

        items[left_idx] = items[pivot_idx - 1]
        items[pivot_idx - 1] = pivot_value
        items[pivot_idx] = item
        pivot_idx -= 1

    return pivot_idx


def _sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = _pivot_idx(items, begin_index, end_index)
    _sort_all(items, begin_index, pivot_index - 1)
    _sort_all(items, pivot_index + 1, end_index)


def quicksort(items):
    _sort_all(items, 0, len(items) - 1)


###########################################################


def quick_sort(collection: List) -> List:
    """
    Implementing quick sort, but not sorting inplace
    """
    if len(collection) < 2:
        return collection

    pivot = collection.pop()
    greater = list()
    lesser = list()

    for element in collection:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


test0 = [1, 0]
test1 = [96, 97, 98]
test2 = [8, 3, 1, 7, 0, 10, 2]

# assert that lists have now been sorted after being called
quicksort(test0)
assert test0 == sorted(test0)
quicksort(test1)
assert test1 == sorted(test1)
quicksort(test2)
assert test2 == sorted(test2)

test3 = [2, 3]
test4 = [101, 102, 103]
test5 = [8, 3, 1, 7, 0, 10, 2]

# this quick sort destroys the existing list so cannot be compared to original
assert quick_sort(test3) == [2, 3]
assert quick_sort(test4) == [101, 102, 103]
assert quick_sort(test5) == [0, 1, 2, 3, 7, 8, 10]
