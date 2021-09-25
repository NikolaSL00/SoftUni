# Write a program which prints a set of elements.
# On the first line, you will receive two numbers - n and m,
# separated by a single space - they represent the lengths of two separate sets.
# On the next n + m lines you will receive n numbers, which are the numbers in the first set,
# and m numbers, which are in the second set. Find all the unique elements that appear in both and print
# them on separate lines (the order does not matter).

# For example:
# Set with length n = 4: {1, 3, 5, 7}
# Set with length m = 3: {3, 4, 5}
# Set that contains all the elements that repeat in both sets -> {3, 5}

# INPUT:
# 4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5

# OUTPUT:
# 3
# 5


# INPUT:
# 2 2
# 1
# 3
# 1
# 5

# OUTPUT:
# 1

length_of_first_set, length_of_second_set = map(int, input().split())

first_set = {int(input()) for _ in range(length_of_first_set)}
second_set = {int(input()) for _ in range(length_of_second_set)}

result_set = first_set & second_set
for el in result_set:
    print(el)
