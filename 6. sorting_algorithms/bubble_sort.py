from typing import List, Tuple


def bubble_sort(arr: List[int]) -> List[int]:
    """sort array from smallest to largest"""
    n = len(arr)
    for iteration in range(n):
        for idx in range(1, n):
            element = arr[idx]
            prev = arr[idx - 1]

            if prev <= element:
                continue

            else:  # swap
                arr[idx] = prev
                arr[idx - 1] = element
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
    for iteration in range(n):
        for idx in range(0, n - 1):
            element = arr[idx]
            nxt = arr[idx + 1]

            if nxt[0] < element[0] or (nxt[0] == element[0] and nxt[1] <= element[1]):
                continue

            else:  # swap
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
