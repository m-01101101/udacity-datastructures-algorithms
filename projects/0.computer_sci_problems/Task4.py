# from Task0 import calls_t, texts_t
import re
import csv

with open("texts.csv", "r") as f:
    # columns = [sending telephone number(string),
    #           receiving telephone number(string),
    #           timestamp of text message(string)]
    reader = csv.reader(f)
    texts = list(reader)
    texts_t = sorted([tuple(i) for i in texts], key=lambda text: text[2])

with open("calls.csv", "r") as f:
    # columns = [calling telephone number(string),
    #           receiving telephone number(string),
    #           start timestamp of telephone call(string),
    #           duration of telephone call in seconds(string)]

    reader = csv.reader(f)
    calls = list(reader)
    calls_t = sorted([tuple(i) for i in calls], key=lambda call: call[2])

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# can't chain extends as list is None type
unique_texters = [i[0] for i in texts_t]
unique_texters.extend([i[1] for i in texts_t])
unique_texters.extend([i[1] for i in calls_t])
# tried this as a generator but didn't keep values unique, seems inefficient
telemarketers = [
    re.sub("[() ]", "", i[0]) for i in calls_t if i[0] not in set(unique_texters)
]

print("These numbers could be telemarketers: ")
print(*sorted(set(telemarketers)), sep="\n")
