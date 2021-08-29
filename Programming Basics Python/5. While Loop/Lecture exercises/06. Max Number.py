# Напишете програма, която до получаване на командата "Stop", чете цели числа,
# въведени от потребителя,  намира най-голямото измежду тях и го принтира.
# Въвежда се по едно число на ред.

# input:
# 100
# 99
# 80
# 70
# Stop
# expected output:
# 100

# input:
# -10
# 20
# -30
# Stop
# expected output:
# 20

import sys

input_number = input()
max_number = -sys.maxsize

while input_number != "Stop":
    if int(input_number) > max_number:
        max_number = int(input_number)
    input_number = input()
print(max_number)
