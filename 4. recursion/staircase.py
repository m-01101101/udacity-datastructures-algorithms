"""
Problem Statement

Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. 
In how many possible ways can you climb the staircase if the staircase has n steps? 
Write a recursive function to solve the problem.

Example:
n == 1 then answer = 1

n == 3 then answer = 4
The output is 4 because there are four ways we can climb the staircase:
1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
3 steps

n == 5 then answer = 13
"""

"""
param: n - number of steps in the staircase
Return number of possible ways in which you can climb the staircase
"""
# not right
def staircase(n):
    
    if n == 1:
        return 1

    else:
        output = 0
        
        for i in range(1, n):
            # output.append([i % n + 1] * (n + 1 // i))
            # output.append([i % n] * (n // i))
            output += (n // (i % n))

        staircase(n-1)

    return output


def udacity_staircase(n):
    """
    :param: n - number of steps in the staircase
    Return number of possible ways in which you can climb the staircase
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        climb_ways = 0
        climb_ways += staircase(n - 1)
        climb_ways += staircase(n - 2)
        climb_ways += staircase(n - 3)

        return climb_ways

