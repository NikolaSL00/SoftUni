# First, you will be given two sequences of integers values on different lines.
# The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
# "Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# "Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# "Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# "Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# "Check Subset" - check if any of the given sequences is a subset of the other. If it is, print "True".
# Otherwise, print "False".
# At the end print the final sequences, separated by a comma and a space ", ".
# The values in each sequence should be sorted in ascending order.

# INPUT:
# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset

# OUTPUT:
# True
# 1, 2, 3, 4, 5, 6
# 1, 2, 3

# INPUT:
# 5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5

# OUTPUT:
# False
# 2, 3, 4, 5, 6, 9
# 6

def check_if_subset(first_line_with_unique_values, second_line_with_unique_values):
    print(first_line_with_unique_values.issubset(second_line_with_unique_values) or second_line_with_unique_values.issubset(first_line_with_unique_values))


first_line_with_unique_values = {int(x) for x in input().split()}
second_line_with_unique_values = {int(x) for x in input().split()}

isSubset = False
number_of_commands = int(input())

for _ in range(number_of_commands):
    command_list = input().split()

    operation = command_list[0]
    collection = command_list[1]

    if operation == "Check":
        check_if_subset(first_line_with_unique_values, second_line_with_unique_values)

    else:
        numbers = [int(command_list[x]) for x in range(2, len(command_list))]

    if collection == "First":

        if operation == "Add":
            [first_line_with_unique_values.add(el) for el in numbers]
        else:
            [first_line_with_unique_values.remove(el) for el in numbers if el in first_line_with_unique_values]

    elif collection == "Second":

        if operation == "Add":
            [second_line_with_unique_values.add(el) for el in numbers]
        else:
            [second_line_with_unique_values.remove(el) for el in numbers if el in second_line_with_unique_values]

print(", ".join([str(el) for el in sorted(first_line_with_unique_values)]))
print(", ".join([str(el) for el in sorted(second_line_with_unique_values)]))
