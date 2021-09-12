from typing import Dict
import re
import csv

with open("calls.csv", "r") as f:
    # columns = [calling telephone number(string),
    #           receiving telephone number(string),
    #           start timestamp of telephone call(string),
    #           duration of telephone call in seconds(string)]

    reader = csv.reader(f)
    calls = list(reader)
    calls_t = sorted([tuple(i) for i in calls], key=lambda call: call[2])

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

The list of codes should be print out one per line in lexicographic order with no duplicates.   
"""
area_codes = [
    re.split("[) ]", i[1].strip("(")) for i in calls_t if i[0].startswith("(080)")
]
area_codes_ = {i[0] if i[0].startswith("0") else i[0][:4] for i in area_codes}
area_codes_.add("140")  # i've assumed a telemarketer was called, should check

print("The numbers called by people in Bangalore have codes:")
print(*sorted(area_codes_), sep="\n")

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

The percentage should have 2 decimal digits
"""

Bang2Bang = len([i for i in area_codes if i[0] == "080"]) * 100 / len(area_codes)

print(
    f"{round(Bang2Bang,2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
)
