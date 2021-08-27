# Млад програмист разполага с определен бюджет и свободно време в даден сезон.
# Напишете програма, която да приема на входа бюджета и сезона,
# а на изхода да изкарва къде ще почива програмистът и колко ще похарчи.
# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи.
# Ако е лято ще почива на къмпинг, а зимата в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел.
# Всеки къмпинг или хотел, според дестинацията, има собствена цена, която отговаря на даден процент от бюджета:

# ⦁	При 100 лв. или по-малко - някъде в България:
# ⦁	Лято - 30% от бюджета;
# ⦁	Зима - 70% от бюджета.
# ⦁	При 1000 лв. или по малко - някъде на Балканите:
# ⦁	Лято - 40% от бюджета;
# ⦁	Зима - 80% от бюджета.
# ⦁	При повече от 1000 лв. - някъде из Европа:
# ⦁	При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.

# Вход
# Входът се чете от конзолата и се състои от два реда, въведени от потребителя:
# ⦁	Бюджет - реално число;
# ⦁	Един от двата възможни сезона - "summer” или "winter”.

# Изход
# На конзолата трябва да се отпечатат два реда:
# ⦁	 "Somewhere in [дестинация]" измежду "Bulgaria", "Balkans" и "Europe"
# ⦁	"{Вид почивка} - {Похарчена сума}":
# ⦁	Почивката може да е между "Camp" и "Hotel"
# ⦁	Сумата трябва да бъде форматирана с точност до вторият знак след десетичната запетая

# input:
# 50
# summer
# expected output:
# Somewhere in Bulgaria
# Camp - 15.00

# input:
# 75
# winter
# expected output:
# Somewhere in Bulgaria
# Hotel - 52.50

# input:
# 312
# summer
# expected output:
# Somewhere in Balkans
# Camp - 124.80

budget = float(input())
season = input()

destination = "N/A"
spent_money = 0
place = "N/A"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        spent_money = 0.30 * budget
    else:
        place = "Hotel"
        spent_money = 0.70 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        spent_money = 0.40 * budget
    else:
        place = "Hotel"
        spent_money = 0.80 * budget
elif budget > 1000:
    destination = "Europe"
    spent_money = 0.90 * budget
    place = "Hotel"
print(f"Somewhere in {destination}")
print(f"{place} - {spent_money:.2f}")
