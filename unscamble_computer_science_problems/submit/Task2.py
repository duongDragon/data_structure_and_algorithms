"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import operator
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
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

# ## The correct answer for this task:- (080)33251027 spent the longest time, 90456 seconds, on the phone during September 2016.

dictionary = {}
for call in calls:
    for phone in call[:2]:
        dictionary[phone] = dictionary.get(phone, 0) + int(call[3])
longest_call_duration = max(dictionary.items(), key=operator.itemgetter(1))

print(longest_call_duration[0], 'spent the longest time,', longest_call_duration[1],
      'seconds, on the phone during September 2016.')