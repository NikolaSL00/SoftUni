# You will have to find all possible color combinations that can be used.
# Write a program that finds colors in a string. You will be given a string on a single line containing substrings (separated by a single space) from which you will be able to form the following colors:
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check if you can get any of the above colors' names. If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed for its creation could be formed from the given substrings:
# orange = red + yellow
# purple = red + blue
# green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found.
# When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and return them in the middle of the original string. If the string contains an odd number of substrings, you should put the substrings one position ahead.
# For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye", so you should remove the last character and return them in the middle of the string: "r by yellow".
# At the end, print out the list with colors in the order in which they are found.
# Input
# Single line string
# Output
# The list with the collected colors
# Constrains
# You will not receive an empty string
# Please consider only the colors mentioned above
# There won't be any cases with repeating colors


# INPUT:
# d yel blu e low redd

# OUTPUT:
# ['yellow', 'blue', 'red']

# INPUT:
# r ue nge ora bl ed

# OUTPUT:
# ['red', 'blue']


# INPUT:
# re ple blu pop e pur d

# OUTPUT:
# ['red', 'purple', 'blue']

from collections import deque

main_colors_dict = {
    "red": False,
    "yellow": False,
    "blue": False
}

secondary_colors_dict = {
    "orange": ("red", "yellow"),
    "purple": ("red", "blue"),
    "green": ("yellow", "blue")
}

collection_with_colors = deque(input().split())

collected_colors = []
secondary_colors_collected = deque()

count = 0

while collection_with_colors:
    first_part = collection_with_colors[0]
    if len(collection_with_colors) > 1:
        second_part = collection_with_colors[-1]
    else:
        second_part = ""

    potentially_color1 = first_part + second_part
    potentially_color2 = second_part + first_part

    if potentially_color1 in main_colors_dict:
        count += 1
        main_colors_dict[potentially_color1] = True
        collected_colors.append((potentially_color1, count))
        collection_with_colors.pop()
        if collection_with_colors:
            collection_with_colors.popleft()

    elif potentially_color2 in main_colors_dict:
        count += 1
        main_colors_dict[potentially_color2] = True
        collected_colors.append((potentially_color2, count))
        collection_with_colors.pop()
        if collection_with_colors:
            collection_with_colors.popleft()

    elif potentially_color1 in secondary_colors_dict:
        count += 1
        secondary_colors_collected.append((potentially_color1, count))
        collection_with_colors.pop()
        collection_with_colors.popleft()

    elif potentially_color2 in secondary_colors_dict:
        count += 1
        secondary_colors_collected.append((potentially_color2, count))
        collection_with_colors.pop()
        collection_with_colors.popleft()

    else:
        first_part = collection_with_colors.popleft()
        if collection_with_colors:
            second_part = collection_with_colors.pop()
        else:
            second_part = ""

        first_part = first_part[:-1]
        second_part = second_part[:-1]

        middle = int(len(collection_with_colors) / 2)

        length_of_first = len(first_part)
        length_of_second = len(second_part)

        if len(first_part) > 0 >= len(second_part):
            collection_with_colors.insert(middle, first_part)

        elif len(first_part) > 0 and len(second_part) > 0:
            collection_with_colors.insert(middle, first_part)
            collection_with_colors.insert(middle + 1, second_part)

        elif len(first_part) <= 0 < len(second_part):
            collection_with_colors.insert(middle, second_part)

if not secondary_colors_collected:
    print(list([x[0] for x in collected_colors]))
else:

    secondary_colors_collected_filtered = []

    for el in secondary_colors_collected:
        tuple_of_main_colors = secondary_colors_dict[el[0]]
        first_main_color_flag = main_colors_dict[tuple_of_main_colors[0]]
        second_main_color_flag = main_colors_dict[tuple_of_main_colors[1]]

        if first_main_color_flag and second_main_color_flag:
            secondary_colors_collected_filtered.append(el)

    result_list = []

    for index in range(1, count + 1):

        if collected_colors:
            tuple1 = collected_colors[0]
            if index == tuple1[1]:
                result_list.append(tuple1[0])
                collected_colors.remove(tuple1)

        if secondary_colors_collected_filtered:
            tuple2 = secondary_colors_collected_filtered[0]
            if index == tuple2[1]:
                result_list.append(tuple2[0])
                secondary_colors_collected_filtered.remove(tuple2)
    print(result_list)
