# На осемнадесетия си рожден ден Хосе взел решение, че ще се изнесе да живее на квартира.
# Опаковал багажа си в кашони и намерил подходяща обява за апартамент под наем.
# Той започва да пренася своя багаж на части, защото не може наведнъж.
# Има ограничено свободно пространство в новото си жилище, където може да разположи вещите,
# така че мястото да бъде подходящо за живеене.
# Напишете програма, която изчислява свободния обем от жилището на Хосе, който остава, след като пренесе багажа си.
# Всеки кашон е с точни размери:  1m x 1m x 1m.

# Вход
# Потребителят въвежда следните данни на отделни редове:
# ⦁	Широчина на свободното пространство - цяло число;
# ⦁	Дължина на свободното пространство - цяло число;
# ⦁	Височина на свободното пространство - цяло число;
# ⦁	На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа
# Програмата трябва да приключи прочитането на данни при команда "Done" или ако свободното място свърши.

# Изход
# Да се отпечата на конзолата един от следните редове:
# ⦁	Ако стигнете до командата "Done" и има още свободно място:
# "{брой свободни куб. метри} Cubic meters left."
# ⦁	Ако свободното място свърши преди да е дошла команда "Done":
# "No more free space! You need {брой недостигащи куб. метри} Cubic meters more."

# input:
# 10
# 10
# 2
# 20
# 20
# 20
# 20
# 122
# expected output:
# No more free space! You need 2 Cubic meters more.

# input:
# 10
# 1
# 2
# 4
# 6
# Done
# expected output:
# 10 Cubic meters left.

width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

cubic_free_space = width_free_space * length_free_space * height_free_space

more_boxes = 0
count_boxes = 0

while count_boxes < cubic_free_space:
    more_boxes = input()
    if more_boxes == "Done":
        print(f"{cubic_free_space - count_boxes} Cubic meters left.")
        break
    else:
        count_boxes += int(more_boxes)
else:
    print(f"No more free space! You need {count_boxes - cubic_free_space} Cubic meters more.")
