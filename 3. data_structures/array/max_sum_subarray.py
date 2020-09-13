"""
You have been given an array containg numbers.
Find and return the largest sum in a contiguous subarray within the input array.

arr = [1, 2, 3, -4, 6]
The largest sum is `8`, which is the sum of all elements of the array.

arr = [1, 2, -5, -4, 1, 6]
The largest sum is `7`, which is the sum of the last two elements of the array.

-----

The process, sum through a list on element at a time.
Decide if adding the value will increase the sum, ie is the number postive.
If the number is positive, keep going.
If the number is negative, store current score and start afresh at the next number.
Will work poorly, if all numbers are negative.
"""

from typing import List


def _max_sum_subarray1(arr: List[int]) -> int:
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    running_total = 0
    placeholder = []
    placeholder.append(sum(arr))  # take into account total sum

    for i in arr:
        if i > 0:
            running_total += i
        elif i < 0:
            placeholder.append(running_total)
            running_total = 0

    placeholder.append(running_total)

    return max(placeholder)


"""
The approach of handling negatives was too blunt

For example;
arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
_max_sum_subarray1(arr)  # returns 15
correct output is 18, [15, -13, 14, -1, 2, 1]

What I need to do was evaluate the current sum I had, 
added to the next element, versus that element alone
"""

# Solution
"""
The Idea:
1. We have to find the sum of "contiguous" subarray, therefore we must not change the order of array elements.
2. Let `current_sum` denotes the sum of a subarray, and `max_sum` denotes the maximum value of `current_sum`.
3. LOOP STARTS: For each element of the array, update the `current_sum` with the MAXIMUM of either:
 - The element added to the `current_sum` (denotes the addition of the element to the current subarray)
 - The element itself  (denotes the starting of a new subarray)
 - Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
4. Return `max_sum`
"""


def max_sum_subarray(arr):

    current_sum = arr[0]  # `current_sum` denotes the sum of a subarray
    max_sum = arr[0]  # `max_sum` denotes the maximum value of `current_sum` ever

    # Loop from VALUE at index position 1 till the end of the array
    for element in arr[1:]:

        """
        # Compare (current_sum + element) vs (element)
        # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
        # If (element) alone is higher, it denotes the starting of a new subarray
        """
        current_sum = max(current_sum + element, element)

        # (overwrite) `max_sum`, if it is lower than the updated `current_sum`
        max_sum = max(current_sum, max_sum)

    return max_sum
