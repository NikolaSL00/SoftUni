# Write a program that extracts all elements from a given sequence of words that are present in it an odd number of times (case-insensitive).
# ⦁	Words are given on a single line, space separated.
# ⦁	Print the result elements in lowercase, in their order of appearance.

# INPUT:
# Java C# PHP PHP JAVA C java

# OUTPUT:
# java c# c

# INPUT:
# 3 5 5 hi pi HO Hi 5 ho 3 hi pi

# OUTPUT:
# 5 hi

# INPUT:
# a a A SQL xx a xx a A a XX c

# OUTPUT:
# a sql xx c

sequence_of_words = input().split(" ")
dict_app = dict()

for el in sequence_of_words:
    el_lower = el.lower()

    if el_lower not in dict_app:
        dict_app[el_lower] = 0
    dict_app[el_lower] += 1

for key, value in dict_app.items():
    if value % 2 != 0:
        print(key, end=" ")
