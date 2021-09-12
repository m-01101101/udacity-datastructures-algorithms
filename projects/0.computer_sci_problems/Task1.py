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
TASK 1:
How many different telephone numbers are there in the records? 
"""

unique_n_calls = {i[0] for i in calls_t}.union({i[1] for i in calls_t})
unique_n_texts = {i[0] for i in texts_t}.union({i[1] for i in texts_t})
unique_numbers = unique_n_calls.union(unique_n_texts)

print(f"There are {len(unique_numbers)} different telephone numbers in the records.")
