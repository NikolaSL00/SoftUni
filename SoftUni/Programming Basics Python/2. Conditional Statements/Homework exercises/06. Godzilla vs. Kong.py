# Снимките за дългоочаквания филм "Годзила срещу Конг" започват.
# Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли,
# дали предвидените средства са достатъчни за снимането на филма.
# За снимките  ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# ⦁	Декорът за филма е на стойност 10% от бюджета.
# ⦁	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Вход
# От конзолата се четат 3 реда:
# ⦁	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# ⦁	Брой на статистите – цяло число в интервала [1 … 500]
# ⦁	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
# Изход
# На конзолата трябва да се отпечатат два реда:
# ⦁	Ако  парите за декора и дрехите са повече от бюджета:
# ⦁	"Not enough money!"
# ⦁	"Wingard needs {парите недостигащи за филма} leva more."
# ⦁	Ако парите за декора и дрехите са по малко или равни на бюджета:
# ⦁	"Action!"
# ⦁	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.

# input:
# 20000
# 120
# 55.5
# expected output:
# Action!
# Wingard starts filming with 11340.00 leva left.


# input:
# 15437.62
# 186
# 57.99
# expected output:
# Action!
# Wingard starts filming with 4186.33 leva left.

# input:
# 9587.88
# 222
# 55.68
# expected output:
# Not enough money!
# Wingard needs 2495.77 leva more.

budget = float(input())
number_statist = int(input())
price_clothes_per_statist = float(input())

decor = budget * 0.1
sum_statist_bill = price_clothes_per_statist * number_statist

if number_statist > 150:
    sum_statist_bill = sum_statist_bill * 0.9

sum_bill = decor + sum_statist_bill

if sum_bill > budget:
    diff = sum_bill - budget
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
elif budget >= sum_bill:
    diff = budget - sum_bill
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")