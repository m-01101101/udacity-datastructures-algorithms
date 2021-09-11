"""
A palindrome is a string that reads the same backwards as forwards, e.g., `MADAM`.

A subsequence is an ordered set of characters that need not necessarily be a contiguous substring, 
    e.g., `ABC` is a subsequence in `AXBYC` with `length = 3`. 

Examples:
    - With an input string, `MAXDYAM`, the LPS is `MADAM`, which has `length = 5`
    - With an input string, `BxAoNxAoNxA`, the LPS is `ANANA`, which has `length = 5`
    - With an input string, `BANANO`, the LPS is `NAN`, which has `length = 3`
    - With an input string, `ABBDBCACB`, the LPS is `BCACB`, which has `length = 5`


Approach:
- For a string of length *n* characters, you can build an `n x n` matrix. 
    The 2-D matrix will have characters of the given string on the top as well as on the left side.
- The matrix will store the solution to **smaller subproblems** first, and gradually adding up more characters to the problem. 
    In this case, **a subproblem is to find the length of the LPS, up to a certain point in the string**.     

input_string = 'BANANO'
  
     B  A  N  A  N  O
B  [[1, 1, 1, 3, 3, 3],
A   [0, 1, 1, 3, 3, 3],
N   [0, 0, 1, 1, 3, 3],
A   [0, 0, 0, 1, 1, 1],
N   [0, 0, 0, 0, 1, 1],
O   [0, 0, 0, 0, 0, 1]]

>>> LPS length:  3


input_string = 'TACOCAT'

     T  A  C  O  C  A  T
T  [[1, 1, 1, 1, 3, 5, 7],
A   [0, 1, 1, 1, 3, 5, 5],
C   [0, 0, 1, 1, 3, 3, 3],
O   [0, 0, 0, 1, 1, 1, 1],
C   [0, 0, 0, 0, 1, 1, 1],
A   [0, 0, 0, 0, 0, 1, 1],
T   [0, 0, 0, 0, 0, 0, 1]]

>>> LPS length:  7    
"""

import pprint

pp = pprint.PrettyPrinter()

# complete LPS solution
def lps(input_string):
    n = len(input_string)

    # create a lookup table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]

    # strings of length 1 have LPS length = 1
    for i in range(n):
        L[i][i] = 1

    # consider all substrings
    for s_size in range(2, n + 1):
        for start_idx in range(n - s_size + 1):
            end_idx = start_idx + s_size - 1
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2
                L[start_idx][end_idx] = 2
            elif input_string[start_idx] == input_string[end_idx]:
                # general match case
                L[start_idx][end_idx] = L[start_idx + 1][end_idx - 1] + 2
            else:
                # no match case, taking the max of two values
                L[start_idx][end_idx] = max(
                    L[start_idx][end_idx - 1], L[start_idx + 1][end_idx]
                )

    # debug line
    # pp.pprint(L)

    return L[0][n - 1]  # value in top right corner of matrix
