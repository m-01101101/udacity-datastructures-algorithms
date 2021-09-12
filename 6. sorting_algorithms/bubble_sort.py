from typing import List, Tuple


def bubble_sort(arr: List[int]) -> List[int]:
    """sort array from smallest to largest"""
    n = len(arr)
    for _ in range(n):
        swapped = False
        for idx in range(1, n):
            if arr[idx - 1] <= arr[idx]:
                continue
            swapped = True
            arr[idx - 1], arr[idx] = arr[idx], arr[idx - 1]
        if not swapped:
            break  # stop iteration as arr sorted
    return arr


wakeup_times = [
    16,
    49,
    3,
    12,
    56,
    49,
    55,
    22,
    13,
    46,
    19,
    55,
    46,
    13,
    25,
    56,
    9,
    48,
    45,
]

assert list(sorted(wakeup_times)) == bubble_sort(wakeup_times)


def bubble_sort2(arr: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """sort tuples from largest to smallest"""
    n = len(arr)
    for _ in range(n):
        for idx in range(n - 1):
            element = arr[idx]
            nxt = arr[idx + 1]

            if nxt[0] < element[0] or (nxt[0] == element[0] and nxt[1] <= element[1]):
                continue

            arr[idx] = nxt
            arr[idx + 1] = element
    return arr


sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]

bubble_sort2(sleep_times)
assert sleep_times == [
    (24, 23),
    (24, 13),
    (24, 3),
    (23, 20),
    (22, 5),
    (21, 58),
    (21, 55),
]
