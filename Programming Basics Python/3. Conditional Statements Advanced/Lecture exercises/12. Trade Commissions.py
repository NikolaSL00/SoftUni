# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:

# Град	0 ≤ s ≤ 500	500 < s ≤ 1 000	1 000 < s ≤ 10 000	s > 10 000
# Sofia	    5%	          7%	        8%	        12%
# Varna 	4.5%	     7.5%	        10%	        13%
# Plovdiv	5.5%	      8%	        12%	        14.5%

# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число),
# въведени от потребителя, и изчислява и извежда размера на търговската комисионна според горната таблица.
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка.
# При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".

# input:
# Sofia
# 1500
# expected output:
# 120.00

# input:
# Plovdiv
# 499.99
# expected output:
# 27.50

# input:
# Varna
# 3874.50
# expected output:
# 387.45

city = input()
number_sales = float(input())
commision = 0

if city == "Sofia":
    if 0 <= number_sales <= 500:
        commision = number_sales * 0.05
        print(f"{commision:.2f}")
    elif 500 < number_sales <= 1000:
        commision = number_sales * 0.07
        print(f"{commision:.2f}")
    elif 1000 < number_sales <= 10000:
        commision = number_sales * 0.08
        print(f"{commision:.2f}")
    elif number_sales > 10000:
        commision = number_sales * 0.12
        print(f"{commision:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= number_sales <= 500:
        commision = number_sales * 0.045
        print(f"{commision:.2f}")
    elif 500 < number_sales <= 1000:
        commision = number_sales * 0.075
        print(f"{commision:.2f}")
    elif 1000 < number_sales <= 10000:
        commision = number_sales * 0.1
        print(f"{commision:.2f}")
    elif number_sales > 10000:
        commision = number_sales * 0.13
        print(f"{commision:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= number_sales <= 500:
        commision = number_sales * 0.055
        print(f"{commision:.2f}")
    elif 500 < number_sales <= 1000:
        commision = number_sales * 0.08
        print(f"{commision:.2f}")
    elif 1000 < number_sales <= 10000:
        commision = number_sales * 0.12
        print(f"{commision:.2f}")
    elif number_sales > 10000:
        commision = number_sales * 0.145
        print(f"{commision:.2f}")
    else:
        print("error")
else:
    print("error")
