def reverse_string(input: str) -> str:
    """
    Return reversed input string
    """
    if len(input) == 0:
        return ""

    else:
        # this scales O(k * n)
        # because we're making a copy each time
        # the reverse function is recursively called to slice the part of the string except the first character and concatenate the first character to the end of the sliced string.
        return reverse_string(input[1:]) + input[0]


def udacity_reverse_string(input):

    # (Recursion) Termination condition / Base condition
    if len(input) == 0:
        return ""

    else:
        first_char = input[0]

        """
        The `slice()` function can accept upto the following three arguments.
        - start: [OPTIONAL] starting index. Default value is 0.
        - stop: ending index (exclusive)
        - step_size: [OPTIONAL] the increment size. Default value is 1.
        
        The return type of `slice()` function is an object of class 'slice'. 
        """
        the_rest = slice(1, None)  # `the_rest` is an object of type 'slice' class
        sub_string = input[the_rest]  # convert the `slice` object into a list

        # Recursive call
        reversed_substring = reverse_string(sub_string)

        return reversed_substring + first_char
