# Напишете програма, която пресмята колко общо пари има в сметката,
# след като направите определен брой вноски.
# На всеки ред ще получавате сумата, която трябва да внесете в сметката до получаване на команда “NoMoreMoney”.
# При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата
# (форматирана до втория знак след десетичната запетая) и тя да се прибавя в сметката.
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!" и програмата да приключи.
# Когато програмата приключи трябва да се принтира "Total: " +
# общата сума в сметката закръглена до втория знак след десетичната запетая.

# input:
# 5.51
# 69.42
# 100
# NoMoreMoney
# expected output:
# Increase: 5.51
# Increase: 69.42
# Increase: 100.00
# Total: 174.93

# input:
# 120
# 45.55
# -150
# expected output:
# Increase: 120.00
# Increase: 45.55
# Invalid operation!
# Total: 165.55

input_sum = input()
account_sum = 0
while input_sum != "NoMoreMoney":
    if float(input_sum) < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {float(input_sum):.2f}")
        account_sum += float(input_sum)
        input_sum = input()
print(f"Total: {account_sum:.2f}")
