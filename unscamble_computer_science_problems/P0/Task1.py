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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

length = len(texts)
telephones = []

if length < len(calls):
    length = len(calls)

for i in range(length):
    telephones.append(texts[i][0])
    telephones.append(texts[i][1])
    if len(calls) <= i:
        continue
    else:
        telephones.append(calls[i][0])
        telephones.append(calls[i][1])

# way 1
# telephones = list(set(telephones))

# way 2
telephones_distinct = []
for phone in telephones:
    if phone not in telephones_distinct:
        telephones_distinct.append(phone)

count = str(len(telephones_distinct))
print("There are " + count + " different telephone numbers in the records.")