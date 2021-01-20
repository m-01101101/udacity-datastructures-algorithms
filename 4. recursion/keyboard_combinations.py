"""
A keypad on a cellphone has alphabets for all numbers between 2 and 9

You can make different combinations of alphabets by pressing the numbers.

For example, if you press 23, the following combinations are possible:

`ad, ae, af, bd, be, bf, cd, ce, cf`

Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2.
Likewise, if the user types 32, the order would be

`da, db, dc, ea, eb, ec, fa, fb, fc`

Given an integer `num`, 
    find out all the possible strings that can be made using digits of input `num`. 
Return these strings in a list. 
The order of strings in the list does not matter. 
However, as stated earlier, the order of letters in a particular string matters.
"""

from typing import List

# given function
# personally, i'd do this as a dictionary
def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num: int) -> List["str"]:

    if num == None or num == 0:  # base case
        return [""]

    elif num < 10:  # n is a single value
        # extract each character associated with key to single element in a list
        return [n for n in get_characters(num)]

    else:
        # get characters for the last number of num
        # example 937 % 10 -> 7
        last_digit_characters = get_characters(num % 10)
        # increment num to avoid recursion
        # example 937 // 10 -> 93
        increment_num = keypad(num // 10)

        # example:
        # 937 % 10 -> 7
        # 937 // 10 -> 93
        # 93 % 10 -> 3
        # 93 // 10 -> 9
        # 9 % 10 -> 9
        # 9 // 10 -> 0

        output = []
        """
        The Idea:
        Each character of keypad_string (i_a) must be appended to the 
        end of each string available in `increment_num`
        """
        for i_a in last_digit_characters:
            for i_b in increment_num:
                output.append(i_b + i_a)  # we're working back to front

        return output


def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        return True
    else:
        return False


# Base case: list with empty string
input = 0
expected_output = [""]
assert test_keypad(input, expected_output) == True

# Example case
input = 23
expected_output = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
assert test_keypad(input, expected_output) == True

# Example case
input = 32
expected_output = sorted(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
assert test_keypad(input, expected_output) == True

# Example case
input = 8
expected_output = sorted(["t", "u", "v"])
assert test_keypad(input, expected_output) == True

input = 354
expected_output = sorted(
    [
        "djg",
        "ejg",
        "fjg",
        "dkg",
        "ekg",
        "fkg",
        "dlg",
        "elg",
        "flg",
        "djh",
        "ejh",
        "fjh",
        "dkh",
        "ekh",
        "fkh",
        "dlh",
        "elh",
        "flh",
        "dji",
        "eji",
        "fji",
        "dki",
        "eki",
        "fki",
        "dli",
        "eli",
        "fli",
    ]
)
assert test_keypad(input, expected_output) == True
