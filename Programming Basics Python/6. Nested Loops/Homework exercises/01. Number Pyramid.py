# Напишете програма, която чете цяло число n, въведено от потребителя, и отпечатва пирамида
# от числа като в примерите:

# input:
# 7
# expected output:
# 1
# 2 3
# 4 5 6
# 7

# input:
# 10
# expected output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# input:
# 12
# expected output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12

# input:
# 15
# expected output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = int(input())
print_count = 0

all_printed = False

for rows in range(1, n + 1):
    for columns in range(1, rows + 1):

        print(print_count+1, end=" ")
        print_count += 1
        if print_count == n:
            all_printed = True
            break
    if all_printed:
        break
    print()