# Write a program which finds the longest intersection.
# You will be given a number N. On each of the next N lines you will be given two ranges in the format:
# "{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these two ranges.
# The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections,
# print the numbers that are included and its length in the format:
# "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be intersection. If there are two equal intersections,
# print the first one.

# INPUT:
# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10

# OUTPUT:
# Longest intersection is [6, 7, 8, 9, 10] with length 5


# INPUT:
# 5
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11

# OUTPUT:
# Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9

number_of_lines = int(input())

max_range_set = set()
for _ in range(number_of_lines):
    first_range, second_range = input().split("-")

    start_of_first_range, end_of_first_range = map(int, first_range.split(","))
    start_of_second_range, end_of_second_range = map(int, second_range.split(","))

    all_range = [start_of_second_range, start_of_first_range, end_of_first_range, end_of_second_range]
    all_range.sort()
    this_range = [int(x) for x in range(all_range[1], all_range[2] + 1)]
    if len(max_range_set) < len(this_range):
        max_range_set = this_range

print(f"Longest intersection is [{', '.join(map(str, max_range_set))}] with length {len(max_range_set)}")
