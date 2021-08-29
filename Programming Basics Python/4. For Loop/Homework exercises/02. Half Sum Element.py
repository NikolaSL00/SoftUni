# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,
# и проверява дали сред тях съществува число, което е равно на сумата на всички останали.

# Ако има такъв елемент, печата
#  "Yes"
# "Sum = "  + неговата стойност ,иначе печата
# "No"
#  "Diff = " + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност).

# input:
# 7
# 3
# 4
# 1
# 1
# 2
# 12
# 1
# expected output:
# Yes
# Sum = 12

# input:
# 4
# 6
# 1
# 2
# 3
# expected output:
# Yes
# Sum = 6

import sys

count = int(input())
max_number = -sys.maxsize
sum_numbers = 0

for n in range(0, count):
    number = int(input())
    if number > max_number:
        max_number = number
    sum_numbers += number
if max_number * 2 == sum_numbers:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number - (sum_numbers - max_number))}")
