# Да се напише програма, която чете скорост (реално число),
# въведена от потребителя и отпечатва информация за скоростта.
# При скорост до 10 (включително) отпечатайте “slow”.
# При скорост над 10 и до 50 отпечатайте “average”. При скорост над 50 и до 150 отпечатайте “fast”.
# При скорост над 150 и до 1000 отпечатайте “ultra fast”. При по-висока скорост отпечатайте “extremely fast”.
# Примери:

# input:
# 8
# expected output:
# slow

# input:
# 49.5
# expected output:
# average

# input:
# 126
# expected output:
# fast

speed = float(input())

if speed <= 10:
    print("slow")
elif speed <= 50:
    print("average")
elif speed <= 150:
    print("fast")
elif speed <= 1000:
    print("ultra fast")
else:
    print("extremely fast")