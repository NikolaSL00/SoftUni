# Иван решава да подобри Световния рекорд по плуване на дълги разстояния.
# На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри,
# разстоянието в метри, което трябва да преплува и времето в секунди, за което плува разстояние от 1 м.
# Да се напише програма, която изчислява дали се е справил със задачата, като се има предвид,
# че: съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
# Когато се изчислява колко пъти Иванчо ще се забави,
# в резултат на съпротивлението на водата, резултатът трябва да се закръгли надолу до най-близкото цяло число.

# Да се изчисли времето в секунди, за което Иванчо ще преплува разстоянието и разликата спрямо Световния рекорд.
# Вход
# От конзолата се четат 3 реда:
# ⦁	Рекордът в секунди – реално число;
# ⦁	Разстоянието в метри – реално число;
# ⦁	Времето в секунди, за което плува разстояние от 1 м. - реално число.
# Изход
# Отпечатването на конзолата зависи от резултата:
# ⦁	Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
# ⦁	" Yes, he succeeded! The new world record is {времето на Иван} seconds."
# ⦁	Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
# ⦁	"No, he failed! He was {недостигащите секунди} seconds slower."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

# input:
# 10464
# 1500
# 20
# expected output:
# No, he failed! He was 20786.00 seconds slower.

# input:
# 55555.67
# 3017
# 5.03
# expected output:
# Yes, he succeeded! The new world record is 17688.01 seconds.

import math

world_record_seconds = float(input())
distance_meters = float(input())
seconds_per_one_meter = float(input())
num_late = 0

ivancho_time = distance_meters * seconds_per_one_meter

if distance_meters >= 15:
    num_late = distance_meters // 15
    math.floor(num_late)

ivancho_time += num_late * 12.5

if ivancho_time < world_record_seconds:
    print(f" Yes, he succeeded! The new world record is {ivancho_time:.2f} seconds.")
else:
    diff = ivancho_time - world_record_seconds
    print(f"No, he failed! He was {diff:.2f} seconds slower.")