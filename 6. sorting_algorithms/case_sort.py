def case_sort(string: str) -> str:
    """
    given a string consistent of ascii character
    sort the uppercase and lowercase characters separately

    Input: fedRTSersUXJ  
    Output: deeJRSfrsTUX
    """
    sorted_string = sorted(string)
    lower_idx = min([i[0] for i in enumerate(sorted(string)) if 97 <= ord(i[1]) <= 122])
    upper_idx = 0  # upper comes before lower, so we can assume 0

    output = list()
    for e in string:
        if 97 <= ord(e) <= 122:
            output.append(sorted_string[lower_idx])
            lower_idx += 1
        elif 65 <= ord(e) <= 90:
            output.append(sorted_string[upper_idx])
            upper_idx += 1

    return "".join(output)


assert case_sort("fedRTSersUXJ") == "deeJRSfrsTUX"
assert case_sort("defRTSersUXI") == "deeIRSfrsTUX"
