# Write a program to read an integer n and print all triples of the first n small Latin letters,
# ordered alphabetically:


# INPUT:
# 3

# EXPECTED OUTPUT:
# aaa
# aab
# aac
# aba
# abb
# abc
# aca
# acb
# acc
# baa
# bab
# bac
# bba
# bbb
# bbc
# bca
# bcb
# bcc
# caa
# cab
# cac
# cba
# cbb
# cbc
# cca
# ccb
# ccc


number = int(input())

for n in range(97, 97 + number):
    for n1 in range(97, 97 + number):
        for n2 in range(97, 97 + number):
            print(f"{chr(n)}{chr(n1)}{chr(n2)}")
