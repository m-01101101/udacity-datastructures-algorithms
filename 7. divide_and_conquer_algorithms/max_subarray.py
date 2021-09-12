def maxCrossingSum(arr: List[int], start: int, mid: int, stop: int):
    """Helper Function - Find the max crossing sum w.r.t. middle index"""
    leftSum = arr[mid]  # start point
    leftMaxSum = arr[mid]  # Keep track of maximum sum
    # Traverse in reverse direction from (mid-1) to start
    for i in range(mid - 1, start - 1, -1):
        leftSum = leftSum + arr[i]
        if leftSum > leftMaxSum:
            leftMaxSum = leftSum

    rightSum = arr[mid + 1]  # start point
    rightMaxSum = arr[mid + 1]  # keep track of maximum sum
    # Traverse in forward direction from (mid+2) to stop
    for j in range(mid + 2, stop + 1):
        rightSum = rightSum + arr[j]
        if rightSum > rightMaxSum:
            rightMaxSum = rightSum

    return rightMaxSum + leftMaxSum


def maxSubArrayRecursive(arr, start, stop):
    """Recursive function"""
    # Base case
    if start == stop:
        return arr[start]

    if start >= stop:  # If ever start > stop. Not feasible.
        return nums[start]

    mid = (start + stop) // 2  # Get the middle index
    L = maxSubArrayRecursive(arr, start, mid)  # Recurse on the Left part
    R = maxSubArrayRecursive(arr, mid + 1, stop)  # Recurse on the Right part
    C = maxCrossingSum(
        arr, start, mid, stop
    )  # Find the max crossing sum w.r.t. middle index
    return max(C, max(L, R))  # Return the maximum of (L,R,C)


def maxSubArray(arr):
    start = 0  # staring index of original array
    stop = len(arr) - 1  # ending index of original array
    return maxSubArrayRecursive(arr, start, stop)


t1 = [-2, 7, -6, 3, 1, -4, 5, 7]
assert maxSubArray(t1) == 13

t2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
assert maxSubArray(t1) == 6

t3 = [-4, 14, -6, 7]
assert maxSubArray(t1) == 15

t4 = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
assert maxSubArray(t4) == 10

t5 = [-2, -5, 6, -2, -3, 1, 5, -6]
assert maxSubArray(t5) == 7
