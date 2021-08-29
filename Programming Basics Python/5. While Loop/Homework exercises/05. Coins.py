# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко
# монети ресто. Напишете програма, която приема сума - рестото,
# което трябва да се върне и изчислява с колко най-малко монети може да стане това.

# input:
# 1.23
# expected output:
# 4

# input:
# 2
# expected output:
# 1

# input:
# 0.56
# expected output:
# 3

# import math

resto = float(input())

coin_2 = 2

coin_1 = 1

coin_0_5 = 0.50

coin_0_2 = 0.20

coin_0_1 = 0.10

coin_0_05 = 0.05

coin_0_02 = 0.02

coin_0_01 = 0.01

used_coins = 0

while resto != 0.00:

    if resto >= coin_2:
        resto -= coin_2
        used_coins += 1

    elif resto >= coin_1:
        resto -= coin_1
        used_coins += 1

    elif resto >= coin_0_5:
        resto -= coin_0_5
        used_coins += 1

    elif resto >= coin_0_2:
        resto -= coin_0_2
        used_coins += 1

    elif resto >= coin_0_1:
        resto -= coin_0_1
        used_coins += 1

    elif resto >= coin_0_05:
        resto -= coin_0_05
        used_coins += 1

    elif resto >= coin_0_02:
        resto -= coin_0_02
        used_coins += 1

    elif resto >= coin_0_01:
        resto -= coin_0_01
        used_coins += 1
    resto = round(resto, 2)
else:
    print(used_coins)
