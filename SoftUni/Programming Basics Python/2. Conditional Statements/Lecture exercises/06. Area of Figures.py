# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура
# и пресмята лицето й. Фигурите са четири вида: квадрат (square), правоъгълник (rectangle),
# кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата (square, rectangle, circle или triangle):

# ⦁	Ако фигурата е квадрат, на следващия ред се чете едно число - дължина на страната му;
# ⦁	Ако фигурата е правоъгълник, на следващите два реда четат две числа - дължините на страните му;
# ⦁	Ако фигурата е кръг, на следващия ред чете едно число - радиусът на кръга;
# ⦁	Ако фигурата е триъгълник, на следващите два реда четат две числа - дължината на страната му и дължината на височината към нея.
# Резултатът да се закръгли до 3 цифри след десетичната точка.

# input:
# square
# 5
# expected output:
# 25.000

# input:
# rectangle
# 7
# 2.5
# expected output:
# 17.500

# input:
# circle
# 6
# expected output:
# 113.097


import math

figure = input()
# square, rectangle, circle or triangle
if figure == "square":
    a = float(input())
    square = a ** 2
    print(f"{square:.3f}")
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    square = a * b
    print(f"{square:.3f}")
elif figure == "circle":
    r = float(input())
    square = math.pi * r ** 2
    print(f"{square:.3f}")
elif figure == "triangle":
    h = float(input())
    a = float(input())
    square = h * a / 2
    print(f"{square:.3f}")