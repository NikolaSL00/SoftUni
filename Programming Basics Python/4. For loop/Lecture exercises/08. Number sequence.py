# Напишете програма, която чете n на брой цели числа.
# Принтирайте най-голямото и най-малкото число сред въведените.

# input:
# 5
# 10
# 20
# 304
# 0
# 50
# expected output:
# Max number: 304
# Min number: 0

# input:
# 6
# 250
# 5
# 2
# 0
# 100
# 1000
# expected output:
# Max number: 1000
# Min number: 0

count = int(input())
min = 1000
max = -1000
for n in range(0, count):
    number = int(input())
    if number > max:
        max = number
    if number < min:
        min = number
print(f"Max number: {max}")
print(f"Min number: {min}")
