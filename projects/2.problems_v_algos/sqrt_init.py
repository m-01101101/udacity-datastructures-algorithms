def sqrt(number: int) -> int:
    if number in {0, 1}:
        return number

    low = 0
    high = number // 2 + 1
    _result = None

    while high >= low:
        mid = (low + high) // 2
        sq = mid * mid

        if sq == number:
            return mid

        elif sq < number:
            low = mid + 1
            _result = mid  # ensure we have floor value to return

        elif sq > number:
            high = mid - 1

    return _result


assert sqrt(9) == 3
assert sqrt(0) == 0
assert sqrt(16) == 4
assert sqrt(1) == 1
assert sqrt(27) == 5
