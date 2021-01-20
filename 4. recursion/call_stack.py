"""
Given a positive integer n, write a function, print_integers, 
that uses recursion to print all numbers from n to 1.

For example, if n is 4, the function should print 4 3 2 1.

If we use iteration, the solution to the problem is simple. 
We can simply start at 4 and use a loop to print all numbers till 1. 
However, instead of using an iterative approach, our goal is to solve this problem using recursion.
"""

# def print_integers(n):
#     print(n)
#     while n > 1:
#         n -= 1
#         print_integers(n)

"""
results in;
print_integers(4) calls print_integers(3)
  print_integers(3) calls print_integers(2)
    print_integers(2) calls print_integers(1)
      print_integers(1) ends
    print_integers(2) ends
  print_integers(3) calls print_integers(1)
    print_integers(1) ends
  print_integers(3) ends
print_integers(4) calls print_integers(2)
  and so on...
"""


def print_integers(n):
    print(n)
    if n > 1:
        n -= 1
        print_integers(n)


"""
print_integers(4) calls print_integers(3)
  print_integers(3) calls print_integers(2)
    print_integers(2) calls print_integers(1)
      print_integers(1) ends
    print_integers(2) ends
  print_integers(3) ends
print_integers(4) ends
"""

# udacity
def _print_integers(n):
    if n <= 0:
        return
    print(n)
    print_integers(n - 1)


# more pythonic?
def __print_integers(n):
    if n > 0:
        print(n)
        print_integers(n - 1)
