from typing import List


def heapify(arr: List[int], n: int, i: int):
    # Using i as the index of the current node, find the 2 child nodes
    #   (if the array were a binary tree)
    #   and find the largest value.
    # If one of the children is larger swap the values and recurse into that subtree

    # consider current index as largest
    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    # compare with left child
    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    # if either of left / right child is the largest node
    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]

        heapify(arr, n, largest_index)


def heapsort(arr):
    # First convert the array into a maxheap by calling heapify on each node, starting from the end
    # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.  Continue to do this until the whole
    # array is sorted
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):  # only need range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


test0 = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
heapsort(test0)
assert test0 == sorted(test0)

test1 = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
heapsort(test1)
assert test1 == sorted(test1)

test2 = [0, 1, 2, 5, 12, 21, 0]
heapsort(test2)
assert test2 == sorted(test2)
