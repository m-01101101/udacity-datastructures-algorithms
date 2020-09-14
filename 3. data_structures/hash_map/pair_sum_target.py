"""
Given an `input_list` and a `target`, return the pair of indices in the list that holds the values which sum to the `target`. 

For example:
`input_list = [1, 5, 9, 7]` and `target = 8`, the answer would be `[0, 3]`,  1 + 7 = 8

The best solution takes O(n) time. This means that you cannot traverse the given list more than once.

Assume that the list does not have any duplicates.
"""
from typing import List


def pair_sum_to_target(input_list: List[int], target: int) -> List[int]:
    """Returns the index of two numbers in a last that when added equal the target"""

    # rubbish approach, would be take one index at a time and return when you get a match
    base_number = 0
    while True:
        for i in range(len(input_list)):
            if input_list[base_number] + input_list[i] == target:
                return [base_number, i]

        base_number += 1


def test_function(test_case):
    output = pair_sum_to_target(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        True
    else:
        False


test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
assert test_function(test_case_1) == True

test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
assert test_function(test_case_2) == True

test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
assert test_function(test_case_3) == True


def fast_pair_sum_to_target(input_list, target):
    """Returns the index of two numbers in a last that when added equal the target"""
    # Create a dictionary.
    # Each element of the input_list would become a "key", and
    # the corresponding index in the input_list would become the "value"
    index_dict = dict()

    for index, element in enumerate(input_list):

        # element + (element - target) = target
        # if this value in the list then that + element = target
        if (target - element) in index_dict:  # this is why we assume no duplicates
            return [index_dict[target - element], index]

        index_dict[element] = index

    return [-1, -1]


# could i use map(lambda, input_list)?
