def prod(a: int, b: int) -> int:
    return a * b


def fact_gen():
    """generates factorials for a number n
    using a recursive function"""
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        i += 1
        n = output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product


# Test block
my_gen = fact_gen()
num = 5
for _ in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120
