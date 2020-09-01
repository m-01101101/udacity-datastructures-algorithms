"""
Define a procedure, `deep_reverse`, that takes as input a list, 
and returns a new list that is the deep reverse of the input list.

This means it reverses all the elements in the list, 
    and if any of those elements are lists themselves, 
    reverses all the elements in the inner list, all the way down. 

>Note: The procedure must not change the input list itself.

Example
Input: `[1, 2, [3, 4, 5], 4, 5]`
Output: `[5, 4, [5, 4, 3], 2, 1]`
"""

def deep_reverse(arr):
    output = []

    for _ in list(reversed(arr)):
        if type(_) == list:
            output.append(deep_reverse(_))
        elif type(_) != list:
            output.append(_)

    return output

# cleaner solution, feels more pythonic?
def _deep_reverse(arr):
    if type(arr) is not list:
        return arr
    else:
        results = []
        arr = arr[::-1]  # more pythonic way to reverse
        for element in arr:
            results.append(deep_reverse(element))
        return results


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)
    if output == solution:
        return True
    else:
        return False

arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
assert test_function(test_case) == True

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
assert test_function(test_case) == True

arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
assert test_function(test_case) == True

arr =  [1, [2,3], 4, [5,6]]
solution = [ [6,5], 4, [3, 2], 1]
test_case = [arr, solution]
assert test_function(test_case) == True
