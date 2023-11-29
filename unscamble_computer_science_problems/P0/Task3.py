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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A:
codes = []
percentage = 0
for call in calls:
    if call[0][1:4] == "080" or call[0][:1] in ("7", "8", "9") or call[0][:3] == "140":
        if call[0][1:4] == "080":
            percentage += 1
        codes.append(call[0])

codes = list(set(codes))
for code in codes:
    print(code)

# Part B:
percentage = "{:.2f}".format(percentage / len(calls) * 100)
print(percentage + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")