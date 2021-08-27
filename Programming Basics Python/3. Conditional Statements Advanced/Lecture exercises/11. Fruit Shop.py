# Магазин за плодове през работните дни работи на следните цени:

# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.50	1.20	0.85	1.45	2.70	5.50	3.85

# През събота и неделя магазинът работи на по-високи цени:

# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.70	1.25	0.90	1.60	3.00	5.60	4.20

# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя,
# и пресмята цената според цените от таблиците по-горе:

# ⦁	плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# ⦁	ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# ⦁	количество (реално число).

# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка.
# При невалиден ден от седмицата или невалидно име на плод да се отпечата "error".

# input:
# apple
# Tuesday
# 2
# expected output:
# 2.40

# input:
# orange
# Sunday
# 3
# expected output:
# 2.70

fruit = input()
day = input()
quantity = float(input())
price = 0

if day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = quantity * 2.70
        print(f'{price:.2f}')
    elif fruit == "apple":
        price = quantity * 1.25
        print(f'{price:.2f}')
    elif fruit == "orange":
        price = quantity * 0.90
        print(f'{price:.2f}')
    elif fruit == "grapefruit":
        price = quantity * 1.60
        print(f'{price:.2f}')
    elif fruit == "kiwi":
        price = quantity * 3.00
        print(f'{price:.2f}')
    elif fruit == "pineapple":
        price = quantity * 5.60
        print(f'{price:.2f}')
    elif fruit == "grapes":
        price = quantity * 4.20
        print(f'{price:.2f}')
    else:
        print("error")
elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" :
    if fruit == "banana":
        price = quantity * 2.50
        print(f'{price:.2f}')
    elif fruit == "apple":
        price = quantity * 1.20
        print(f'{price:.2f}')
    elif fruit == "orange":
        price = quantity * 0.85
        print(f'{price:.2f}')
    elif fruit == "grapefruit":
        price = quantity * 1.45
        print(f'{price:.2f}')
    elif fruit == "kiwi":
        price = quantity * 2.70
        print(f'{price:.2f}')
    elif fruit == "pineapple":
        price = quantity * 5.50
        print(f'{price:.2f}')
    elif fruit == "grapes":
        price = quantity *3.85
        print(price)
    else:
        print("error")
else:
    print("error")

