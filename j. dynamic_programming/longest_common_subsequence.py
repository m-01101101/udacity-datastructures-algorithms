"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence
present in both of them.  A subsequence is a sequence that appears in the same relative
order, but not necessarily continuous.
Example:"abc", "abg" are subsequences of "abcdefgh".
"""


def lcs(string_a, string_b):

    # initialize the matrix
    lookup_table = [
        [0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)
    ]

    # enumerate(str) returns a tuple containing the index and character in each iteration
    for char_a_i, char_a in enumerate(string_a):

        for char_b_i, char_b in enumerate(string_b):

            # If there is a match,
            # fill that grid cell with the value to the top-left of that cell plus one
            if char_a == char_b:
                lookup_table[char_a_i + 1][char_b_i + 1] = (
                    lookup_table[char_a_i][char_b_i] + 1
                )

            # If there is not a match,
            # take the maximum value from either directly to the left or the top cell
            else:
                lookup_table[char_a_i + 1][char_b_i + 1] = max(
                    lookup_table[char_a_i][char_b_i + 1],
                    lookup_table[char_a_i + 1][char_b_i],
                )

    # the bottom-right cell will hold the non-normalized LCS length value.
    return lookup_table[-1][-1]


test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print("LCS val 1 = ", lcs_val1)
assert lcs_val1 == 5, "Incorrect LCS value."
print("LCS val 2 = ", lcs_val2)
assert lcs_val2 == 7, "Incorrect LCS value."
print("Tests passed!")

################################################

from typing import Tuple


def longest_common_subsequence(x: str, y: str) -> Tuple[int, str]:
    """
    Finds the longest common subsequence between two strings. Also returns the
    The subsequence found
    Parameters
    ----------
    x: str, one of the strings
    y: str, the other string
    Returns
    -------
    L[m][n]: int, the length of the longest subsequence. Also equal to len(seq)
    Seq: str, the subsequence found
    >>> longest_common_subsequence("programming", "gaming")
    (6, 'gaming')
    >>> longest_common_subsequence("physics", "smartphone")
    (2, 'ph')
    >>> longest_common_subsequence("computer", "food")
    (1, 'o')
    """
    # find the length of strings

    assert x is not None
    assert y is not None

    m = len(x)
    n = len(y)

    # declaring the array for storing the dp values
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                match = 1
            else:
                match = 0

            L[i][j] = max(L[i - 1][j], L[i][j - 1], L[i - 1][j - 1] + match)

    seq = ""
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            match = 1
        else:
            match = 0

        if L[i][j] == L[i - 1][j - 1] + match:
            if match == 1:
                seq = x[i - 1] + seq
            i -= 1
            j -= 1
        elif L[i][j] == L[i - 1][j]:
            i -= 1
        else:
            j -= 1

    return L[m][n], seq
