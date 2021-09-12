"""
Given an input string, return all permutations of the string in an array.

Example 1:
* `string = 'ab'`
* `output = ['ab', 'ba']`

Example 2:
* `string = 'abc'`
* `output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']`

Strings in Python are immutable, 
    which means that we cannot overwrite the characters of the String objects.
    we can only re-assign the variable to a new value (string)
    therefore, we do not require a deep copy

The Idea
Starting with a blank list, add each character of original input string at all possible positions.

For example, take `"abc"` as the original string:
1. Start with a blank `list()` object. 
    This is actually the last call of recursive function stack. 
    Pick a character `'c'` of original string, making the output as `['c']`
2. Pick next character `b` of original input string, 
    and place the current character at different indices of the each sub-string of previous output.
    We can make use of the sub-string of previous output, to create a new sub-string.
    Now, the output will become `['bc', 'cb']`.
3. Pick next character `a` of original input string, 
    and place the current character at different indices of the each sub-string of previous output. 
    Now, the output will become `['abc', 'bac', 'bca', 'acb', 'cab', 'cba']`.
"""
from typing import List


def _string_permutations_attempt1(string: str) -> List[str]:
    output = []
    if len(string) == 0:
        output.append("")
    else:
        character = string[-1]
        alt_string = string[:-1]

        sub_output = string_permutations_attempt1(alt_string)

        for sub_string in sub_output:
            for _ in range(len(sub_string) + 1):
                character += sub_string
                output.append(character)

    return output


def _string_permutations_attempt2(string: str) -> List[str]:
    output = []
    if len(string) == 0:
        output.append("")
    else:
        character = string[-1]
        alt_string = string[:-1]

        sub_output = string_permutations_attempt2(alt_string)

        for sub_string in sub_output:
            print(f"substring is: {sub_string}, sub_output is: {sub_output}")
            for _ in range(len(string)):  # gives me correct length of output
                character += sub_string
                print(
                    f"substring is: {sub_string}, sub_output is: {sub_output}, character is {character}"
                )
                output.append(character)

    return output


"""
debug

substring is: , sub_output is: ['']
substring is: , sub_output is: [''], character is a
substring is: a, sub_output is: ['a']
substring is: a, sub_output is: ['a'], character is ba
substring is: a, sub_output is: ['a'], character is baa
substring is: ba, sub_output is: ['ba', 'baa']
substring is: ba, sub_output is: ['ba', 'baa'], character is cba
substring is: ba, sub_output is: ['ba', 'baa'], character is cbaba
substring is: ba, sub_output is: ['ba', 'baa'], character is cbababa
substring is: baa, sub_output is: ['ba', 'baa']
substring is: baa, sub_output is: ['ba', 'baa'], character is cbabababaa
substring is: baa, sub_output is: ['ba', 'baa'], character is cbabababaabaa
substring is: baa, sub_output is: ['ba', 'baa'], character is cbabababaabaabaa

issue is here -> character += sub_string
i need to reset the string, or only be taking a character at a time
"""


def _string_permutations_attempt3(string: str) -> List[str]:
    output = []
    if len(string) == 0:
        output.append("")
    else:
        character = string[-1]
        alt_string = string[:-1]

        sub_output = string_permutations_attempt3(alt_string)

        for sub_string in sub_output:
            for _ in range(len(string)):  # gives me correct length of output
                to_add = character.__add__(sub_string)
                output.append(to_add)

    return output


"""
output
['cba', 'cba', 'cba', 'cba', 'cba', 'cba']

need to use i as an index for where and how to add
"""


def string_permutations(input_str: str) -> List[str]:
    # initialise list to return
    # example case: input_str = 'abc'
    output = []
    if input_str == "":  # base case / exit logic
        output.append("")
    else:
        # take the last character
        # tail_char = 'c'
        tail_char = input_str[-1]
        # shorten the string to prevent infinite recursion
        # tailless_input = 'ab'
        tailless_input = input_str[:-1]

        # do recursion
        sub_output = string_permutations(tailless_input)

        # For each sub output, inject our removed character at all possible string positions
        # tail_char = 'c'
        #                        0       1       2
        # sub_string = 'ab' -> ['cab', 'acb', 'abc']
        for sub_string in sub_output:
            for i in range(len(input_str)):  # gives me correct length of output (n!)
                # use index to insert tail character in the right place
                to_add = sub_string[:i] + tail_char + sub_string[i:]
                output.append(to_add)

    # Return our combined output
    return output


assert string_permutations("abc") == ["cba", "bca", "bac", "cab", "acb", "abc"]


# Recursive Solution
"""
Param - input string
Return - compound object: list of all permutations of the input string
"""


def udacity_string_permutations(string):
    return return_permutations(string, 0)


def return_permutations(string, index):
    # output to be returned
    output = []

    # Terminaiton / Base condition
    if index >= len(string):
        return [""]

    # Recursive function call
    small_output = return_permutations(string, index + 1)

    # Pick a character
    current_char = string[index]

    # Iterate over each sub-string available in the list returned from previous call
    for subString in small_output:

        # place the current character at different indices of the sub-string
        for index in range(len(small_output[0]) + 1):

            # Make use of the sub-string of previous output, to create a new sub-string.
            new_subString = subString[0:index] + current_char + subString[index:]
            output.append(new_subString)

    return output
