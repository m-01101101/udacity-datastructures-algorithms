"""
You have been given an array of `length = n`. 
The array contains integers from `0` to `n - 2`. 
Each number in the array is present exactly once
    except for one number which is present twice. 
Find and return this duplicate number present in the array

**Example:**~
* `arr = [0, 2, 3, 1, 4, 5, 3]`
* `output = 3` (because `3` is present twice)

The expected time complexity for this problem is `O(n)`
The expected space-complexity is `O(1)`
"""
from typing import List


def duplicate_number(arr: List[int]) -> int:
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    return [i for i in arr if arr.count(i) > 1][0]

    # clever
    # expected_sum = sum(list(range(len(arr)-1)))
    # current_sum = sum(arr)
    # return current_sum - expected_sum


def udacity_duplicate_number(arr):
    """
    Notice carefully that
    1. All the elements of the array are always non-negative
    2. If array length = n, then elements would start from 0 to (n-2),
        i.e. Natural numbers 0,1,2,3,4,5...(n-2)
    3. There is only SINGLE element which is present twice.

    Therefore let's find the sum of all elements (current_sum) of the original array,
    and find the sum of first (n-2) Natural numbers (expected_sum).

    Trick:
    The second occurrence of a particular number (say `x`)
        is actually occupying the space  that would have been utilized
        by the number (n-1).
    This leads to:
    current_sum  = 0 + 1 + 2 + 3 + .... + (n-2) + x
    expected_sum = 0 + 1 + 2 + 3 + .... + (n-2)
    current_sum - expected_sum = x
    """
    current_sum = 0
    expected_sum = 0

    # Traverse the original array in the forward direction
    for num in arr:
        current_sum += num

    # Traverse from 0 to (length of array-1) to get the expected_sum
    # Alternatively, you can use the formula for sum of an Arithmetic Progression to get the expected_sum

    # It means that if the array length = n, loop will run form 0 to (n-2)
    for i in range(len(arr) - 1):
        expected_sum += i

    # The difference between the
    return current_sum - expected_sum


def multi_duplicates(arr: List[int]) -> List[int]:
    """
    another approach
    https://www.youtube.com/watch?v=aMsSF1Il3IY
    each element in the array is a valid index
        (i-1, if the list was 1 to n not 0 to n)
    we loop through the list
    and make each value at the corresponding index 0
    so in the example;
    array1 = [4, 2, 3, 1, 4, 0]
    we would turn array1[4] to a negative
    then we know we've seen the value before
    works for finding mulitiple duplicates
    """

    dups = []
    for i in arr:
        i = abs(i)
        if arr[i] < 0:
            dups.append(i)
        else:
            arr[i] *= -1

    return dups


array1 = [1, 2, 3, 4, 3, 4, 5, 6, 2, 0]
assert multi_duplicates(array1) == [3, 4, 2]
