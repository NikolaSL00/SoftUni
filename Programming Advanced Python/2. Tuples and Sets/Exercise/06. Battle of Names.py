# You will receive a number N.
# On the next N lines, you will be receiving names.
# You must sum the ascii values of each letter in the name and integer divide it to the number
# of the current row (starting from 1). Save the result to a set of either odd or even numbers,
# depending on if the devised number is an odd or even. After that, sum the values of each set.

# If the sums of the two sets are equal, print the union of the values, separated by ", ".
# If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values,
# separated by ", ".
# If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric different values,
# separated by ", ".

# NOTE: On every operation, the starting set should be the odd set

# # INPUT:
# 4
# Pesho
# Stefan
# Stamat
# Gosho

# OUTPUT:
# 304, 128, 206, 511


# INPUT:
# 6
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan

# OUTPUT:
# 733, 101

number_of_lines_with_names = int(input())

set_with_odd = set()
set_with_even = set()

for row in range(1, number_of_lines_with_names + 1):
    name = input()
    sum_of_ascii = 0
    for ch in name:
        sum_of_ascii += ord(ch)
    sum_of_ascii //= row
    if sum_of_ascii % 2 == 0:
        set_with_even.add(sum_of_ascii)
    else:
        set_with_odd.add(sum_of_ascii)

result_odd = sum(set_with_odd)
result_even = sum(set_with_even)

if result_odd > result_even:
    symmetric_different_values = set_with_odd.symmetric_difference(set_with_even)
    print(", ".join(map(str, set_with_odd)))
elif result_odd < result_even:
    symmetric_different_values = set_with_odd.symmetric_difference(set_with_even)
    print(", ".join(map(str, symmetric_different_values)))
else:
    new_set = set_with_odd | set_with_even
    print(", ".join(map(str, new_set)))
