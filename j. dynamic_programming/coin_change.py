"""
You have m types of coins available in infinite quantities and a total amount of money

The value of each coins is given in the array `coins = [1, 2, 3]`

Determine the fewest coins needed to make up that amount
"""


def coin_change_recursive(coins, amount):
    # Create a memo that will storing the fewest coins with given amount
    # that we have already calculated so that we do not have to do the
    # calculation again.
    memo = {}

    def return_change(remaining):
        # Base cases
        if remaining < 0:
            return float("inf")
        if remaining == 0:
            return 0

        # Check if we have already calculated
        if remaining not in memo:
            # If not previously calculated, calculate it by calling return_change with the remaining amount
            memo[remaining] = min(return_change(remaining - c) + 1 for c in coins)
        return memo[remaining]

    res = return_change(amount)

    # return -1 when no change found
    return -1 if res == float("inf") else res


def coin_change_iterative(coins, amount):
    # initiate the list with length amount + 1 and prefill with float('inf')
    res = [float("inf")] * (amount + 1)

    # when amount = 0, 0 number of coins will be needed for the change
    res[0] = 0

    for i in range(amount):
        if res[i] != float("inf"):
            for coin in coins:
                if i <= amount - coin:
                    res[i + coin] = min(res[i] + 1, res[i + coin])
    if res[amount] == float("inf"):
        return -1
    return res[amount]


assert coin_change_recursive([1, 2, 5], 11) == 3
assert coin_change_recursive([1, 4, 5, 6], 23) == 4
assert coin_change_recursive([5, 7, 8], 2) == -1
