"""
One of the most interesting Number Patterns is Pascal's Triangle 
(named after Blaise Pascal, a famous French Mathematician and Philosopher)

Each number is the sum of the two numbers directly above it

Find and return the `nth` row of Pascal's triangle in the form a list. `n` is 0-based.

For example, if `n = 4`, then `output = [1, 4, 6, 4, 1]`.

----

My approach
The triangle does not need to be constructed from the ground up
row n, has n + 1 elements, as we start from n = 0 with just 1
We know the sum of each now, n ** 2
We know the triangle is symmetrical
We know the first and last element are 1
Therefore, given n, we should be able to calculate the elements

n ** 2 = sum(n_row)
len(n) = n + 1
n_row[0] == 1 and n_row[-1] == 1

From mathisfun;
Each line is also the powers (exponents) of 11
At 11 ** 5, the digits overlap
"""

from typing import List, Dict


def nth_row_pascal(n: int) -> List[int]:
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    # TODO figure out is this is possible
    nth_row = list(range(n + 1))  # set length of nth row
    nth_row[0] = nth_row[-1] = 1  # set first and last to 1

    # should be taking into account whether odd or even

    filler = (n ** 2 - 2) / (len(nth_row) - 2)
    for i in nth_row[1:-1]:
        nth_row[i] = filler

    return nth_row


def construct_pascal(n: int) -> Dict[int, List[int]]:
    pascal_triangle = {0: [1], 1: [1, 1], 2: [1, 2, 1], 3: [1, 3, 3, 1]}

    for i in range(n + 1):
        try:
            pascal_triangle[i]
        except KeyError:
            pascal_triangle[i] = list(range(i + 1))
            holding = []

            for x, y in enumerate(pascal_triangle[i]):
                try:
                    y = pascal_triangle[i - 1][x - 1] + pascal_triangle[i - 1][x]
                    holding.append(y)
                except IndexError:
                    holding.append(1)
                    pascal_triangle[i] = holding
                    pascal_triangle[i][0] = 1

    return pascal_triangle


assert construct_pascal(9) == {
    0: [1],
    1: [1, 1],
    2: [1, 2, 1],
    3: [1, 3, 3, 1],
    4: [1, 4, 6, 4, 1],
    5: [1, 5, 10, 10, 5, 1],
    6: [1, 6, 15, 20, 15, 6, 1],
    7: [1, 7, 21, 35, 35, 21, 7, 1],
    8: [1, 8, 28, 56, 70, 56, 28, 8, 1],
    9: [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
}


def _nth_row_pascal(n: int) -> List[int]:
    pascal_triangle = construct_pascal(n)

    return pascal_triangle[n]


assert _nth_row_pascal(9) == [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]


# Solution

"""
Points to note:
1. We have to return a list.
2. The elements of n^th row are made up of elements of (n-1)^th row. This comes up till the 1^st row. We will follow a top-down approach. 
3. Except for the first and last element, any other element at position `j` in the current row is the sum of elements at position `j` and `j-1` in the previous row. 
4. Be careful about the edge cases, example, an index should never be a NEGATIVE at any point of time. 
"""


def udacity_nth_row_pascal(n):

    if n == 0:
        return [1]

    current_row = [1]  # First row

    """ Loop from 1 to n; `i` denotes the row number"""
    for i in range(1, n + 1):
        # Set the `current_row` from previous iteration as the `previous_row`
        previous_row = current_row

        # Let's build the fresh current_row gradually
        current_row = [
            1
        ]  # add the default first element at the 0^th index of the `i^th` row

        """Loop from 1 to (i-1); `j` denotes the index of an element with in the `i^th` row"""
        # Example, for 5th row we have considered n=4,
        # we will iterate index from 1 to 3, because
        # the default element at the 0^th index has already been added
        for j in range(1, i):

            # An element at position `j` in the current row is the
            # sum of elements at position `j` and `j-1` in the previous row.
            next_number = previous_row[j] + previous_row[j - 1]

            # Append the new element to the current_row
            current_row.append(next_number)

        current_row.append(1)  # append the default last element
    return current_row


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")
