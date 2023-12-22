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

telephoneMarketing = []
outgoingCalls = []
receiveIncomingcalls = []

for call in calls:
    if call[0] not in outgoingCalls:
        outgoingCalls.append(call[0])
    if call[1] not in receiveIncomingcalls:
        receiveIncomingcalls.append(call[1])

outgoingTexts = []
receiveTexts = []

for text in texts:
    if text[0] not in outgoingTexts:
        outgoingTexts.append(text[0])
    if text[1] not in receiveTexts:
        outgoingTexts.append(text[1])

for number in outgoingCalls:
    if (number not in receiveIncomingcalls) and (number not in outgoingTexts) and (number not in receiveTexts):
        telephoneMarketing.append(number)

print("These numbers could be telemarketers: ")
print(*sorted(telephoneMarketing), sep='\n')