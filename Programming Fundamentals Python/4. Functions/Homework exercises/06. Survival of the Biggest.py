# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones and then, you should print all the numbers that are left in the list,
# separated by a comma and a space ", ".

# INPUT:
# 10 9 8 7 6 5
# 3

# EXPECTED OUTPUT:
# 10, 9, 8


# INPUT:
# 1 10 2 9 3 8
# 2

# EXPECTED OUTPUT:
# 10, 9, 3, 8

list_of_string = input().split(" ")

list_of_integers = []

for string in list_of_string:
    int_n = int(string)
    list_of_integers.append(int_n)

count = int(input())

for _ in range(count):
    min_number = min(list_of_integers)
    list_of_integers.remove(min_number)

string_ints = [str(int) for int in list_of_integers]

str_of_ints = ", ".join(string_ints)
print(str_of_ints)
