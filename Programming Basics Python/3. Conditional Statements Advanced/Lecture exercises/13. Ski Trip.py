# Атанас решава да прекара отпуската си в Банско и да кара ски. Преди да отиде обаче,
# трябва да резервира хотел и да изчисли колко ще му струва престоят.
# Съществуват следните видове помещения със следните цени за престой:

# ⦁	"room for one person" – 18.00 лв за нощувка
# ⦁	"apartment" – 25.00 лв за нощувка
# ⦁	"president apartment" – 35.00 лв за нощувка

# Според броят на дните, в които ще остане в хотела (пример: 11 дни = 10 нощувки) и видът на помещението,
# което ще избере, той може да ползва различно намаление. Намаленията са както следва:

# вид помещение	по-малко от 10 дни	между 10 и 15 дни	повече от 15 дни
# room for one person	не ползва намаление	 не ползва намаление	не ползва намаление
# apartment	30% от крайната цена	35% от крайната цена	50% от крайната цена
# president apartment	10% от крайната цена	15% от крайната цена	20% от крайната цена
# След престоя оценката на Атанас за услугите на хотела може да е позитивна (positive) или негативна (negative) .
# Ако оценката му е позитивна, към цената с вече приспаднатото намаление Атанас добавя 25% от нея.
# Ако оценката му е негативна приспада от цената 10%.

# Входът се чете от конзолата и се състои от три реда:
# ⦁	Първи ред - дни за престой - цяло число;
# ⦁	Втори ред - вид помещение - "room for one person", "apartment" или "president apartment";
# ⦁	Трети ред - оценка - "positive"  или "negative".
#
#
# На конзолата трябва да се отпечата един ред - цената за престоят му в хотела,
# форматирана до втория знак след десетичната запетая.

# input:
# 14
# apartment
# positive
# expected output:
# 264.06

# input:
# 30
# president apartment
# negative
# expected output:
# 730.80

# input:
# 12
# room for one person
# positive
# expected output:
# 247.50

days_on_holiday = int(input())
type_room = input()
grade = input()

nights_on_holiday = days_on_holiday - 1
price_off = 0
price = 0

if type_room == "apartment":
    price = nights_on_holiday * 25
    if days_on_holiday > 15:
        price_off = 0.50
    elif 10 <= days_on_holiday <= 15:
        price_off = 0.35
    elif days_on_holiday < 10:
        price_off = 0.30
    price = price - price_off * price
elif type_room == "president apartment":
    price = nights_on_holiday * 35
    if days_on_holiday > 15:
        price_off = 0.20
    elif 10 <= days_on_holiday <= 15:
        price_off = 0.15
    elif days_on_holiday < 10:
        price_off = 0.10
    price = price - price_off * price
elif type_room == "room for one person":
    price = (nights_on_holiday * 18)

if grade == "positive":
    price += price * 0.25
elif grade == "negative":
    price -= price * 0.1

print(f"{price:.2f}")