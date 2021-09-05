# Trifon has finally become a junior developer and has received his first task.
# It is about manipulating a list of integers. He is not quite happy about it since he hates manipulating lists.
# They are going to pay him a lot of money, though, and he is willing to give somebody half of it if to help him do
# his job. You, on the other hand, love lists (and money) so you decide to try your luck.

# The list may be manipulated by one of the following commands
# exchange {index} – splits the list after the given index and exchanges the places of the two resulting sub-lists.
# E.g. [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]
# If the index is outside the boundaries of the list, print "Invalid index"
# Negative index is considered invalid.
# max even/odd– returns the INDEX of the max even/odd element -> [1, 4, 8, 2, 3] -> max odd -> print 4
# min even/odd – returns the INDEX of the min even/odd element -> [1, 4, 8, 2, 3] -> min even > print 3
# If there are two or more equal min/max elements, return the index of the rightmost one
# If a min/max even/odd element cannot be found, print "No matches"
# first {count} even/odd– returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]
# last {count} even/odd – returns the last {count} elements -> [1, 8, 2, 3] -> last 2 odd -> print [1, 3]
# If the count is greater than the list length, print "Invalid count"
# If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty list "[]"
# end – stop taking input and print the final state of the list

# Input
# The input data should be read from the console.
# On the first line, the initial list is received as a line of integers, separated by a single space
# On the next lines, until the command "end" is received, you will receive the list manipulation commands
# The input data will always be valid and in the format described. There is no need to check it explicitly.

# Output
# The output should be printed on the console.
# On a separate line, print the output of the corresponding command
# On the last line, print the final list in square brackets with its elements separated by a comma and a space
# See the examples below to get a better understanding of your task

# Constraints
# The number of input lines will be in the range [2 … 50].
# The list elements will be integers in the range [0 … 1000].
# The number of elements will be in the range [1 .. 50]
# The split index will be an integer in the range [-231 … 231 – 1]
# first/last count will be an integer in the range [1 … 231 – 1]
# There will not be redundant whitespace anywhere in the input
# Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.


# INPUT:
# 1 3 5 7 9
# exchange 1
# max odd
# min even
# first 2 odd
# last 2 even
# exchange 3
# end

# EXPECTED OUTPUT:
# 2
# No matches
# [5, 7]
# []
# [3, 5, 7, 9, 1]


# INPUT:
# 1 10 100 1000
# max even
# first 5 even
# exchange 10
# min odd
# exchange 0
# max even
# min even
# end

# EXPECTED OUTPUT:
# 3
# Invalid count
# Invalid index
# 0
# 2
# 0
# [10, 100, 1000, 1]


# INPUT:
# 1 10 100 1000
# exchange 3
# first 2 odd
# last 4 odd
# end

# EXPECTED OUTPUT:
# [1]
# [1]
# [1, 10, 100, 1000]


import sys


def is_valid_index(collection: list, index: int):
    if 0 <= index < len(collection):
        return True

    return False


def exchange_list_at_index(collection: list, index: int):
    exchanged_list = []

    if not is_valid_index(collection, index):
        print('Invalid index')
        exchanged_list = collection
    else:
        left_sub_list = collection[:index + 1]
        right_sub_list = collection[index + 1:]

        for el in right_sub_list:
            exchanged_list.append(el)

        for el in left_sub_list:
            exchanged_list.append(el)

    return exchanged_list


def max_num_by_criteria(collection: list, custom_filter):
    # Returns the index of max even/odd element by given filter function.
    # It returns -1 if there is no match
    max_element = float('-inf')
    max_element_index = -1

    for i in range(len(collection)):
        num = collection[i]

        if custom_filter(num) and num >= max_element:
            max_element = num
            max_element_index = i

    if max_element_index == -1:
        # No matches found
        print('No matches')

    return max_element_index


def min_num_by_criteria(collection: list, custom_filter):
    min_element = sys.maxsize
    min_element_index = -1

    for i in range(len(collection)):
        num = collection[i]

        if custom_filter(num) and num <= min_element:
            min_element = num
            min_element_index = i

    if min_element_index == -1:
        print('No matches')

    return min_element_index


def first_count_elements_by_criteria(collection: list, count: int, custom_filter):
    if count > len(collection):
        print('Invalid count')
    else:
        matching_elements = []

        for num in collection:
            if custom_filter(num) and len(matching_elements) < count:
                matching_elements.append(num)

        print(matching_elements)


def last_count_elements_by_criteria(collection: list, count: int, custom_filter):
    if count > len(collection):
        print('Invalid count')
    else:
        matching_elements = []

        for i in range(len(collection) - 1, -1, -1):
            num = collection[i]

            if custom_filter(num) and len(matching_elements) < count:
                matching_elements.append(num)

        print(matching_elements[::-1])


def parse_collection_to_int(collection: list):
    parsed_collection = []

    for el in collection:
        parsed_collection.append(int(el))

    return parsed_collection


def stringify_collection(collection: list, delimiter: str):
    parsed_collection = []

    for num in collection:
        parsed_collection.append(str(num))

    return delimiter.join(parsed_collection)


elements = input().split()
numbers = parse_collection_to_int(elements)

command = input()
while command != "end":
    cmd_args = command.split()
    cmd_type = cmd_args[0]

    if cmd_type == "exchange":
        index = int(cmd_args[1])

        numbers = exchange_list_at_index(numbers, index)
    elif cmd_type == "max":
        cmd_filter = cmd_args[1]

        max_index = -1

        if cmd_filter == "even":
            max_index = max_num_by_criteria(numbers, lambda n: n % 2 == 0)
        elif cmd_filter == "odd":
            max_index = max_num_by_criteria(numbers, lambda n: n % 2 != 0)

        if max_index != -1:
            print(max_index)
    elif cmd_type == "min":
        cmd_filter = cmd_args[1]

        min_index = -1

        if cmd_filter == "even":
            min_index = min_num_by_criteria(numbers, lambda n: n % 2 == 0)
        elif cmd_filter == "odd":
            min_index = min_num_by_criteria(numbers, lambda n: n % 2 != 0)

        if min_index != -1:
            print(min_index)
    elif cmd_type == "first":
        count = int(cmd_args[1])
        cmd_filter = cmd_args[2]

        if cmd_filter == "even":
            first_count_elements_by_criteria(numbers, count, lambda n: n % 2 == 0)
        elif cmd_filter == "odd":
            first_count_elements_by_criteria(numbers, count, lambda n: n % 2 != 0)
    elif cmd_type == "last":
        count = int(cmd_args[1])
        cmd_filter = cmd_args[2]

        if cmd_filter == "even":
            last_count_elements_by_criteria(numbers, count, lambda n: n % 2 == 0)
        elif cmd_filter == "odd":
            last_count_elements_by_criteria(numbers, count, lambda n: n % 2 != 0)

    command = input()

print(f'[{stringify_collection(numbers, ", ")}]')
