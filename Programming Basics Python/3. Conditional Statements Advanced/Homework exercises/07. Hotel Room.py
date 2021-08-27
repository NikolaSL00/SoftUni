# Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма,
# която изчислява цената за целия престой за студио и апартамент. Цените зависят от месеца на престоя:

# Май и октомври	        Юни и септември	            Юли и август
# Студио - 50 лв./нощувка	Студио - 75.20 лв./нощувка	Студио - 76 лв./нощувка
# Апартамент - 65 лв./нощувка	Апартамент - 68.70 лв./нощувка	Апартамент - 77 лв./нощувка

# Предлагат се и следните отстъпки:
# ⦁	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# ⦁	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# ⦁	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# ⦁	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

# Вход
# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
# ⦁	На първия ред е месецът - May, June, July, August, September или October;
# ⦁	На втория ред е броят на нощувките - цяло число.

# Изход
# Да се отпечатат на конзолата 2 реда:
# ⦁	На първия ред: "Apartment: {цена за целият престой} lv."
# ⦁	На втория ред: "Studio: {цена за целият престой} lv."

# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.

# input:
# May
# 15
# expected output:
# Apartment: 877.50 lv.
# Studio: 525.00 lv.

# input:
# June
# 14
# expected output:
# Apartment: 961.80 lv.
# Studio: 1052.80 lv.


month = input()
count_nights = int(input())

total_apartment = 0
total_studio = 0

if month == "May" or month == "October":
    total_studio = count_nights * 50
    total_apartment = count_nights * 65
    if 14 >= count_nights > 7:
        total_studio -= total_studio * 0.05
    if count_nights > 14:
        total_studio -= total_studio * 0.30
        total_apartment -= total_apartment * 0.10

elif month == "June" or month == "September":
    total_studio = 75.20 * count_nights
    total_apartment = 68.70 * count_nights
    if count_nights > 14:
        total_studio -= total_studio * 0.20
        total_apartment -= total_apartment * 0.10
else:
    total_studio = 76 * count_nights
    total_apartment = 77 * count_nights
    if count_nights > 14:
        total_apartment -= total_apartment * 0.10

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
