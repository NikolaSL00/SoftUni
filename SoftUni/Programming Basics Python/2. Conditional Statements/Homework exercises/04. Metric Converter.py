# Да се напише програма, която преобразува разстояние между следните 3 мерни единици: mm, cm, m.
# Използвайте съответствията от таблицата по-долу:
# входна единица	изходна единица
# 1 meter (m)	1000 millimeters (mm)
# 1 meter (m)	100 centimeters (cm)
# Входните данни се състоят от три реда, въведени от потребителя:
# ⦁	Първи ред: число за преобразуване - реално число;
# ⦁	Втори ред: входна мерна единица – текст;
# ⦁	Трети ред: изходна мерна единица (за резултата) – текст.
# На конзолата да се отпечата резултатът от преобразуването на мерните единици,
# форматиран до третия знак след десетичната запетая.

# input:
# 12
# mm
# m
# expected output:
# 0.012

# input:
# 150
# m
# cm
# expected output:
# 15000.000

# input:
# 45
# cm
# mm
# expected output:
# 450.000

number = float(input())
convert_from = input()
convert_to = input()

convert_rate = f"{convert_from}:{convert_to}"
if convert_rate == "mm:cm":
    number = number / 10
elif convert_rate == "mm:m":
    number = number / 1000
elif convert_rate == "cm:m":
    number = number / 100
elif convert_rate == "cm:mm":
    number = number * 10
elif convert_rate == "m:cm":
    number = number * 100
elif convert_rate == "m:mm":
    number = number * 1000

print(f"{number:.3f}")