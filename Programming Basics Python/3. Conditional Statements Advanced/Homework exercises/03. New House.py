# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете програма, която да изчисли колко  ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен. Различните цветя са с различни цени:
# цвете	                Роза	Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	5	    3.80	2.80	3	    2.50

# Съществуват следните отстъпки:
# ⦁	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# ⦁	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# ⦁	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# ⦁	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# ⦁	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

# От конзолата се четат 3 реда:
# ⦁	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# ⦁	Брой цветя - цяло число;
# ⦁	Бюджет - цяло число.

# Да се отпечата на конзолата на един ред:
# ⦁	Ако бюджетът им е достатъчен
# - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# ⦁	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

# input:
# Roses
# 55
# 250
# expected output:
# Not enough money, you need 25.00 leva more.

# input:
# Tulips
# 88
# 260
# expected output:
# Hey, you have a great garden with 88 Tulips and 50.56 leva left.

# input:
# Narcissus
# 119
# 360
# expected output:
# Not enough money, you need 50.55 leva more.

type_flower = input()
count_flowers = int(input())
budget = int(input())

discount = 0
not_discount = 0
price = 0
total = 0

if type_flower == "Roses":
    price = 5
    if count_flowers > 80:
        discount = 0.10
elif type_flower == "Dahlias":
    price = 3.80
    if count_flowers > 90:
        discount = 0.15
elif type_flower == "Tulips":
    price = 2.80
    if count_flowers > 80:
        discount = 0.15
elif type_flower == "Narcissus":
    price = 3
    if count_flowers < 120:
        not_discount = 0.15
elif type_flower == "Gladiolus":
    price = 2.50
    if count_flowers < 80:
        not_discount = 0.20

if discount != 0:
    total = (count_flowers * price) - (count_flowers * price * discount)
elif not_discount != 0:
    total = (count_flowers * price) + (count_flowers * price * not_discount)
else:
    total = count_flowers * price

diff = 0
if budget >= total:
    diff = budget - total
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {diff:.2f} leva left.")
else:
    diff = total - budget
    print(f"Not enough money, you need {diff:.2f} leva more.")

