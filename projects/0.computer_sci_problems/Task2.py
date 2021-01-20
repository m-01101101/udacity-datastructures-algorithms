from typing import Dict
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

unique_n_calls = set(i[0] for i in calls_t).union(set(i[1] for i in calls_t))
unique_n_texts = set(i[0] for i in texts_t).union(set(i[1] for i in texts_t))
unique_numbers = unique_n_calls.union(unique_n_texts)
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
"""
number_calltime = {n: 0 for n in unique_numbers}
for calls in calls_t:
    number_calltime[calls[0]] += float(calls[3])
    number_calltime[calls[1]] += float(calls[3])

num_time = sorted(
    number_calltime.items(), key=lambda num_time: num_time[1], reverse=True
)

print(
    f"{num_time[0][0]} spent the longest time, {num_time[0][1]} seconds, on the phone during September 2016."
)
