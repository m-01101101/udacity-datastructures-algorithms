"""
Read file into texts and calls.
"""
import csv
from typing import List, Tuple


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
TASK 0:
What is the first record of texts and what is the last record of calls?
"""
print(
    f"""
First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}\n
Last record of calls, {calls[-1][0]} calls {calls[-1][1]} at time {calls[-1][2]}, lasting {calls[-1][3]} seconds
"""
)
