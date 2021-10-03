# On the first line, you will receive a command - "Odd" or "Even". You will receive a sequence of numbers (integers) on the second line, separated by a single space.
# If the command is "Odd", print the sum of the odd numbers multiplied by the count of all numbers.
# If the command is "Even", print the sum of the even numbers multiplied by the count of all numbers.

# INPUT:
# Odd
# 1 3 5 34 7 9 12 11 13 10

# OUTPUT:
# 490

# INPUT:
# Even
# 1 3 5 7 9 13

# OUTPUT:
# 0

command = input()
numbers = [int(x) for x in input().split()]
count_of_all_numbers = len(numbers)

if command == "Odd":
    odd_numbers = filter(lambda x: x % 2 != 0, numbers)
    print(sum(odd_numbers) * count_of_all_numbers)
else:
    even = filter(lambda x: x % 2 == 0, numbers)
    print(sum(even) * count_of_all_numbers)
