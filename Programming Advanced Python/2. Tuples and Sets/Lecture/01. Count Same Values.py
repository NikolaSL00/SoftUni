# You will be given numbers separated by a space.
# Write a program that prints the number of occurrences of each number in the format "{number} - {count} times".
# The number must be formatted to the first decimal point.

# INPUT:
# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3

# OUTPUT:
# -2.5 - 3 times
# 4.0 - 2 times
# 3.0 - 4 times
# -5.5 - 1 times


# INPUT:
# 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3

# OUTPUT:
# 2.0 - 3 times
# 4.0 - 6 times
# 5.0 - 4 times
# 3.0 - 7 times

input_string = input()

numbers = [float(x) for x in input_string.split(" ")]

dict = {}

for number in numbers:
    if number in dict:
        dict[number] += 1
    else:
        dict[number] = 1

for key, value in dict.items():
    print(f"{key} - {value} times")
