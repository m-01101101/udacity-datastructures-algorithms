"""Look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time.
Sorting usually requires O(n log n) 
Do not use Python's inbuilt functions to find min and max."""

import random
from typing import List, Tuple


def get_min_max(ints: List[int]):    #  -> Tuple(int, int)
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None

    _min = _max = ints[0]

    for i in ints[1:]:
        if i < _min:
            _min = i
        if i > _max:
            _max = i

    return (_min, _max)


# test case
l = [i for i in range(10)]
random.shuffle(l)
assert get_min_max(l) == (min(l), max(l))

# edge cases
assert(get_min_max([]) is None)
assert(get_min_max([0, 0, 0, 0, 0, 0, 0, 0]) == (0, 0))
