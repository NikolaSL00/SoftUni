# You will receive 2 lines of input. On the first line you will receive a single string of integers,
# separated by a comma and a space ", ". On the second line you will receive a count of beggars.
# Your job is to print a list with the sum of what each beggar brings home, assuming they all take regular turns,
# from the first to the last number in the list.
# For example: [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6,
# as the first one takes [1, 3, 5], the second one collects [2, 4].
# The same list with 3 beggars would produce a better outcome for the second beggar: 5, 7 and 3,
# as they will respectively take [1, 4], [2, 5] and [3].
# Also note that not all beggars have to take the same amount of "offers",
# meaning that the length of the list is not necessarily a multiple of n.
# Length of the list could be even shorter - i.e., the last beggars will take nothing (0).

# INPUT:
# 1 , 2, 3, 4, 5
# 2

# EXPECTED OUTPUT:
# [9, 6]


# INPUT:
# 100, 94, 24, 99
# 5

# EXPECTED OUTPUT:
# [100, 94, 24, 99, 0]

string_of_integers = input()

count_of_beggars = int(input())

list_of_integers = string_of_integers.split(", ")
sum_list = []
sum = 0

if len(list_of_integers) > count_of_beggars:
    for number in range(count_of_beggars):
        for n in range(number, len(list_of_integers), count_of_beggars):
            sum += int(list_of_integers[n])
        sum_list.append(sum)
        sum = 0

elif len(list_of_integers) == count_of_beggars:
    for n in list_of_integers:
        sum_list.append(int(n))
else:
    for n in range(count_of_beggars):
        if len(list_of_integers) > n:
            sum_list.append(int(list_of_integers[n]))
        else:
            sum_list.append(0)
print(sum_list)
