# Предприемчив българин отваря квартални магазинчета в няколко града и продава на различни цени според града:

# град / продукт	coffee	water	beer	sweets	peanuts
# Sofia	            0.50	0.80	1.20	1.45	1.60
# Plovdiv	        0.40	0.70	1.15	1.30	1.50
# Varna	            0.45	0.70	1.10	1.35	1.55

# Напишете програма, която чете продукт (текст), град (текст) и количество (десетично число),
# въведени от потребителя, и пресмята и отпечатва колко струва съответното количество от избрания продукт
# в посочения град.

# input:
# coffee
# Varna
# 2
# expected output:
# 0.9

# input:
# peanuts
# Plovdiv
# 1
# expected output:
# 1.5

# input:
# beer
# Sofia
# 6
# expected output:
# 7.2

product = input()
city = input()
quantity = float(input())
price = 0
if product == "coffee":
    if city == "Varna":
        price = 0.45
    elif city == "Sofia":
        price = 0.50
    elif city == "Plovdiv":
        price = 0.40
elif product == "water":
    if city == "Varna" or city == "Plovdiv":
        price = 0.70
    elif city == "Sofia":
        price = 0.80
elif product == "beer":
    if city == "Varna":
        price = 1.10
    elif city == "Sofia":
        price = 1.20
    elif city == "Plovdiv":
        price = 1.15
elif product == "sweets":
    if city == "Varna":
        price = 1.35
    elif city == "Sofia":
        price = 1.45
    elif city == "Plovdiv":
        price = 1.30
elif product == "peanuts":
    if city == "Varna":
        price = 1.55
    elif city == "Sofia":
        price = 1.60
    elif city == "Plovdiv":
        price = 1.50
price *= quantity
print(price)
