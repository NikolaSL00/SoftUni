# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ.
# Напишете програма, която спрямо времето от денонощието и градусите да препоръча на Виктор какви дрехи да облече.
# Вашият приятел има различни планове за всеки етап от деня,
# които изискват и различен външен вид - може да ги видите от таблицата.

# От конзолата се четат точно два реда:
# ⦁	Градусите - цяло число;
# ⦁	Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".

# Време от денонощието / градуси
# Morning
# Afternoon
# Evening
# 10 <= градуси <= 18	Outfit = Sweatshirt
# Shoes = Sneakers	Outfit = Shirt
# Shoes = Moccasins	Outfit = Shirt
# Shoes = Moccasins
# 18 < градуси <= 24	Outfit = Shirt
# Shoes = Moccasins	Outfit = T-Shirt
# Shoes = Sandals	Outfit = Shirt
# Shoes = Moccasins
# градуси >= 25	Outfit = T-Shirt
# Shoes = Sandals	Outfit = Swim Suit
# Shoes = Barefoot	Outfit = Shirt
# Shoes = Moccasins
#
# Като изход да се отпечата на конзолата на един ред: "It's {градуси} degrees, get your {облекло} and {обувки}."

# input:
# 16
# Morning
# expected output:
# It's 16 degrees, get your Sweatshirt and Sneakers.

# input:
# 22
# Afternoon
# expected output:
# It's 22 degrees, get your T-Shirt and Sandals.

celsium_degrees = int(input())
time_of_day = input()

Outfit = "N/A"
Shoes = "N/A"

if time_of_day == "Morning":
    if 10 <= celsium_degrees <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif 18 < celsium_degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif celsium_degrees >= 25:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
elif time_of_day == "Afternoon":
    if 10 <= celsium_degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif 18 < celsium_degrees <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif celsium_degrees >= 25:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
elif time_of_day == "Evening":
    if 10 <= celsium_degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif 18 < celsium_degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif celsium_degrees >= 25:
        Outfit = "Shirt"
        Shoes = "Moccasins"
print(f"It's {celsium_degrees} degrees, get your {Outfit} and {Shoes}.")
