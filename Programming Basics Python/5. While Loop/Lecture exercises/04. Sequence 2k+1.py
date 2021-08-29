# Напишете програма, която чете число n, въведено от потребителя, и отпечатва всички числа  ≤  n от редицата:
# 1, 3, 7, 15, 31, …. Всяко следващо число се изчислява като умножим предишното с 2 и добавим 1.

# input:
# 3
# expected output:
# 1
# 3

# input:
# 8
# expected output:
# 1
# 3
# 7

n = float(input())
number = 1
while number <= n:
    print(number)
    number = number * 2 + 1
