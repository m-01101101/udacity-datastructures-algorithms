"""
Problem Statement
Given an integer array, find and return all the subsets of the array.
The order of subsets in the output array is not important.
However the order of elements in a particular subset should remain the same as in the input array.

Note:
An empty set will be represented by an empty list.
If there are repeat integers, each occurrence must be treated as a separate entity.

Example 1
arr = [9, 9]

output = [[],
          [9],
          [9],
          [9, 9]]

Example 2
arr = [9, 12, 15]

output =  [[],
           [15],  # arr[len(arr) - 1: len(arr): 1]
           [12],  # arr[len(arr) - 2: len(arr) - 1: 1]
           [12, 15], # arr[len(arr) - 2: len(arr): 1]
           [9], # arr[len(arr) - 3: len(arr) - 2: 1]
           [9, 15],  # arr[len(arr) - 3: len(arr): 2]
           [9, 12],
           [9, 12, 15]]  # arr[len(arr)- len(arr): len(arr)]
"""


def subsets(arr):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    """

    # base condition
    if len(arr) == 1:
        # finalCompoundList.append(arr)
        return [arr]

    else:
        # must results final output after else statement
        # otherwise it resets on final recursion call
        output = list()
        output.append(arr)
        # slice_arr = slice(0, len(arr) - (len(arr) - 1))

        for i in range(len(arr)):
            output.append([arr[i]])  # add i element as list
            temp = arr.copy()
            temp.pop(i)
            output.append(temp)  # add array without i element as list
            subsets(temp)

    return output
