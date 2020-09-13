correct = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

incorrect = [[1, 2, 3, 4], [2, 3, 1, 3], [3, 1, 2, 3], [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]]

incorrect3 = [
    [1, 2, 3, 4, 5],
    [2, 3, 1, 5, 6],
    [4, 5, 2, 1, 3],
    [3, 4, 5, 2, 1],
    [5, 6, 4, 3, 2],
]

incorrect4 = [["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"]]

incorrect5 = [[1, 1.5], [1.5, 1]]


"""
A valid sudoku square satisfies these two properties:

Each column of the square contains each of the whole numbers from 1 to n exactly once.

Each row of the square contains each of the whole numbers from 1 to n exactly once.

Assume that the input is square and contains at least one row and column.
"""


def check_sudoku(square) -> bool:
    # check rows
    for i in square:
        if list(sorted(i)) == list(range(1, len(i) + 1)):
            continue
        else:
            return False

    square_pivoted = []
    for _ in range(len(square[0])):
        square_pivoted.append([i[_] for i in square])
    # check columns
    for i in square_pivoted:
        if list(sorted(i)) == list(range(1, len(i) + 1)):
            continue
        else:
            return False

    return True
