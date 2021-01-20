"""
A palindrome is a word that is the reverse of itself—that is, 
it is the same word when read forwards and backwards.

*  "madam" is a palindrome
* "abba" is a palindrome
*  "cat" is not

Note that this problem can also be solved with a non-recursive solution, but that's not the point
"""


def is_palindrome(input: str) -> bool:
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    if len(input) < 2:  # base case
        return True

    else:
        # this will take the first and last of not just the initial string
        # but all versions of the sub string parsed in to the function
        first = input[0].lower()
        last = input[-1].lower()

        # sub_input is input with first and last char removed
        sub_input = input[1:-1].lower()

        # recursive call, if first and last char are identical, else return False
        return (first == last) and is_palindrome(sub_input)


def isPalindrome(s: str) -> bool:
    """
    Return True if all letters in s produce a palindrome, False otherwise.
    """

    def _toChars(s):
        s = s.lower()
        letters = ""
        for c in s:  # removes non letter characters
            if c in "abcdefghijklmnopqrstuvwyxyz":
                letters += c
        return letters

    def _isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and _isPal(s[1:-1])

    return _isPal(_toChars(s))


assert is_palindrome("") == True
assert is_palindrome("a") == True
assert is_palindrome("abba") == True
assert is_palindrome("madam") == True
assert is_palindrome("Udacity") == False

assert isPalindrome("") == True
assert isPalindrome("a") == True
assert isPalindrome("abba") == True
assert isPalindrome("madam") == True
assert isPalindrome("Udacity") == False
