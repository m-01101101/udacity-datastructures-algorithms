"""
In an encryption system where ASCII lower case letters represent numbers 
    in the pattern a=1, b=2, c=3... and so on,
find out all the codes that are possible for a given input number.

Example 1
number = 123
codes_possible = ["aw", "abc", "lc"]

Explanation: The codes are for the following number:
1 . 23 = "aw"
1 . 2 . 3 = "abc"
12 . 3 = "lc"

Example 2
number = 145
codes_possible = ["ade", "ne"]

Return the codes in a list. The order of codes in the list is not important.

Note: you can assume that the input number will not contain any 0s
"""

from typing import List


def translate_ascii(number):
    """
    Helper function to figure out alphabet of a particular number
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number
    """
    return chr(number + 96)


def all_codes(number: int) -> List[str]:
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    """

    if number == 0:
        return [""]

    # calculation for two right-most digits
    remainder = number % 100
    # must initialise after calc remainder, but before if statement
    output100 = list()
    if remainder <= 26 and number > 9:
        output100 = all_codes(number // 100)

        # translate number to ascii
        # must do this after calling recursive function, otherwise remainder reset
        alphabet = translate_ascii(remainder)
        # cannot then append, as each character will be in the list alone
        # example: 'a', 'w'
        # must combine elements 'aw'
        for index, element in enumerate(output100):
            output100[index] = element + alphabet

    # calculation for right-most digit
    remainder = number % 10
    output10 = all_codes(number // 10)

    # translate number to ascii
    # must do this after calling recursive function, otherwise remainder reset
    alphabet = translate_ascii(remainder)
    # output10.append(get_alphabet(remainder))
    for index, element in enumerate(output10):
        output10[index] = element + alphabet

    output = output10 + output100

    return output
