# Write a program which receives a sequence of numbers (string containing integers separated by ", ")
# and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".

# Examples:
# The numbers 2, 8, 4 and 10 fall into the group of 10's.
# The numbers 13, 19, 14 and 15 fall into the group of 20's.
# For more clarification, see the examples below.


# INPUT:
# 8, 12, 38, 3, 17, 19, 25, 35, 50

# EXPECTED OUTPUT:
# Group of 10's: [8, 3]
# Group of 20's: [12, 17, 19]
# Group of 30's: [25]
# Group of 40's: [38, 35]
# Group of 50's: [50]

# INPUT:
# 1, 3, 3, 4, 34, 35, 25, 21, 33

# EXPECTED OUTPUT:
# Group of 10's: [1, 3, 3, 4]
# Group of 20's: []
# Group of 30's: [25, 21]
# Group of 40's: [34, 35, 33]


numbers = [int(el) for el in input().split(", ")]

max_element = max(numbers)
max_group = (max_element // 10) * 10
if max_element > max_group:
    max_group += 10

for groups in range(1, (max_group // 10) + 1):
    current_group = groups * 10
    group = []
    for el in numbers:
        if current_group - 10 < el <= current_group:
            group.append(el)
    print(f"Group of {current_group}'s: {group}")
