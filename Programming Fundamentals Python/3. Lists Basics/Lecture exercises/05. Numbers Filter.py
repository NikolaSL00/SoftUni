# You will receive a single number n.
# On the next n lines you will receive integers. After that you will be given one of the following commands:
# ⦁	even
# ⦁	odd
# ⦁	negative
# ⦁	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

# INPUT:
# 5
# 33
# 19
# -2
# 18
# 998
# even

# EXPECTED OUTPUT:
# [-2, 18, 998]

# INPUT:
# 3
# 111
# -4
# 0
# negative

# EXPECTED OUTPUT:
# [-4]

number = int(input())

integers = []

for i in range(0, number):
    integers.append(int(input()))
word = input()

result_list = []
for numbers in range(0, len(integers)):
    if word == "even":
        if integers[numbers] % 2 == 0:
            result_list.append(integers[numbers])
    elif word == "odd":
        if not integers[numbers] % 2 == 0:
            result_list.append(integers[numbers])
    elif word == "positive":
        if integers[numbers] >= 0:
            result_list.append(integers[numbers])
    elif word == "negative":
        if integers[numbers] < 0:
            result_list.append(integers[numbers])
print(result_list)
