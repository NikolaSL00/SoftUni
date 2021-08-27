# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони.
# Има три вида прожекции с билети на различни цени:
# ⦁	Premiere - премиерна прожекция, на цена 12.00 лева;
# ⦁	Normal - стандартна прожекция, на цена 7.50 лева;
# ⦁	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа),
# въведени от потребителя, и изчислява общите приходи от билети при пълна зала.
# Резултатът да се отпечата във формат 2 знака след десетичната точка.

# input:
# Premiere
# 10
# 12
# expected output:
# 1440.00 leva

# input:
# Normal
# 21
# 13
# expected output:
# 2047.50 leva

# input:
# Discount
# 12
# 30
# expected output:
# 1800.00 leva

type_projection = input()
count_row = int(input())
count_column = int(input())

price = 0

if type_projection == "Premiere":
    price = 12.00
elif type_projection == "Normal":
    price = 7.50
elif type_projection == "Discount":
    price = 5.00
income = price * count_row * count_column
print(f"{income:.2f}")