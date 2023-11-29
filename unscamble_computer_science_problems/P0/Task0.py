"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

file_path_texts = '/Users/super_dash/Documents/development/data_structure_and_algorithms/unscamble_computer_science_problems/P0/texts.csv'
with open(file_path_texts, 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

file_path_calls = '/Users/super_dash/Documents/development/data_structure_and_algorithms/unscamble_computer_science_problems/P0/calls.csv'
with open(file_path_calls, 'r') as f:
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

