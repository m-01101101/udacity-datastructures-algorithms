# Recursive Solution
"""
Args: myList: list of items to be permuted
Returns: compound list: a list of all possible combinations of the input list
"""
import copy  # We will use `deepcopy()` function from the `copy` module


def list_permutations(inputList):

    # a compound list
    finalCompoundList = []  # compoundList to be returned

    # Termination / Base condition
    if len(inputList) == 0:
        finalCompoundList.append([])

    else:
        first_element = inputList[0]  # Pick one element to be permuted
        after_first = slice(1, None)  # `after_first` is an object of type 'slice' class
        rest_list = inputList[after_first]  # convert the `slice` object into a list

        # Recursive function call
        sub_compoundList = list_permutations(rest_list)

        # Iterate through all lists of the compoundList returned from previous call
        for aList in sub_compoundList:

            # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList) in each iteration
            for j in range(0, len(aList) + 1):

                # A normal copy/assignment will change aList[j] element
                bList = copy.deepcopy(aList)

                # A new list with size +1 as compared to aList
                # is created by inserting the `first_element` at position j in bList
                bList.insert(j, first_element)

                # Append the newly created list to the finalCompoundList
                finalCompoundList.append(bList)

    return finalCompoundList


# Test Cases

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


print("Pass" if (check_output(list_permutations([]), [[]])) else "Fail")
print("Pass" if (check_output(list_permutations([0]), [[0]])) else "Fail")
print("Pass" if (check_output(list_permutations([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print(
    "Pass"
    if (
        check_output(
            list_permutations([0, 1, 2]),
            [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]],
        )
    )
    else "Fail"
)
