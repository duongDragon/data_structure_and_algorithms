"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# First record of texts
incoming_number_text = texts[0][0]
answering_number_text = texts[0][1]
time_text = texts[0][2]
print("First record of texts, " + incoming_number_text + " texts " + answering_number_text + " at time " + time_text)

# Last record of calls
incoming_number_call = calls[-1][0]
answering_number_call = calls[-1][1]
time_call = calls[-1][2]
lasting = calls[-1][3]
print("Last record of calls, " + incoming_number_call + " calls " + answering_number_call + " at time " + time_call + " lasting " + lasting)

