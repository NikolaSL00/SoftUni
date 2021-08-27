# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова,
# че решават да отидат на риболов с кораб. Цената за наема на кораба зависи от сезона и броя рибари:

# В зависимост от сезона:
# ⦁	Цената за наем на кораба през пролетта е  3000 лв.;
# ⦁	Цената за наем на кораба през лятото и есента е  4200 лв.;
# ⦁	Цената за наем на кораба през зимата е  2600 лв.

# В зависимост от броя на групата има различна отстъпка:
# ⦁	Ако групата е до 6 човека включително  -  отстъпка от 10%;
# ⦁	Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# ⦁	Ако групата е от 12 нагоре  -  отстъпка от 25%.

# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.

# Вход
# От конзолата се четат три реда:
# ⦁	Бюджет на групата - цяло число;
# ⦁	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# ⦁	Брой рибари - цяло число.

# Изход
# На конзолата да се отпечата следното:
# ⦁	Ако бюджетът е достатъчен:
# "Yes! You have {останалите пари} leva left."
# ⦁	Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.

# input:
# 3000
# Summer
# 11
# expected output:
# Not enough money! You need 570.00 leva.

# input:
# 3600
# Autumn
# 6
# expected output:
# Not enough money! You need 180.00 leva.

# input:
# 2000
# Winter
# 13
# expected output:
# Yes! You have 50.00 leva left.

budget = int(input())
season = input()
count_fisherman = int(input())

boat_loan = 0
discount_even = 0
discount_count = 0
total = 0

if season == "Spring":
    boat_loan = 3000
    if count_fisherman % 2 == 0:
        discount_even = 0.05
elif season == "Summer" or season == "Autumn":
    boat_loan = 4200
    if count_fisherman % 2 == 0 and season == "Summer":
        discount_even = 0.05
elif season == "Winter":
    boat_loan = 2600
    if count_fisherman % 2 == 0:
        discount_even = 0.05

if count_fisherman <= 6:
    discount_count = 0.10
elif 7 <= count_fisherman <= 11:
    discount_count = 0.15
elif count_fisherman >= 12:
    discount_count = 0.25

total = boat_loan - boat_loan * discount_count
if discount_even != 0:
    total -= total * discount_even

if total <= budget:
     diff = budget - total
     print(f"Yes! You have {diff:.2f} leva left.")
else:
     diff = total - budget
     print(f"Not enough money! You need {diff:.2f} leva.")

