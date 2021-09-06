# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line which are substrings
# of any string in the second input line.


# INPUT:
# arp, live, strong
# lively, alive, harp, sharp, armstrong

# EXPECTED OUTPUT:
# ['arp', 'live', 'strong']


# INPUT:
# tarp, mice, bull
# lively, alive, harp, sharp, armstrong

# EXPECTED OUTPUT:
# []


first_sequence = [el for el in input().split(", ")]
second_sequence = [el for el in input().split(", ")]
subset = []

for sub in first_sequence:
    for el in second_sequence:
        if el.find(sub) != -1:
            subset.append(sub)
            break

print(subset)
