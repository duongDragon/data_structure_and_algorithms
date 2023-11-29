"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call = []
time = 0
for i in range(len(calls)):
    if int(calls[i][3]) > time:
        time = int(calls[i][3])
        call = calls[i]

telephone_number = call[0]
total_time = call[3]

print(telephone_number + " spent the longest time, " + total_time + " seconds, on the phone during September 2016.")