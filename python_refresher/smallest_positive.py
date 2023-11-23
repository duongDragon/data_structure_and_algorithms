# Exercise 1: Smallest Positive
# Finish writing smallest_positive which is a function that finds the smallest positive number in a list.

def smallest_positive(in_list):
    smallest_pos = None
    for num in in_list:
        if num > 0:
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos

# Test cases
print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2
print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2
print(smallest_positive([-6, -9, -7]))
# Correct output: None
print(smallest_positive([]))