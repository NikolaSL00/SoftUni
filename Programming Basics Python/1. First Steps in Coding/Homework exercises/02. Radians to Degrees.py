# Напишете програма, която чете ъгъл в радиани (rad) и го преобразува в градуси (deg).
# Принтирайте получените градуси като цяло число използвайки math.floor.
# Използвайте формулата: градуси = радиани * 180 / π.
# Числото π в Python може да достъпите чрез модула math.
# За да ползвате функционалността му, първо трябва да включите констатата pi.

# input ->    3.1416
# expected output ->  180

# input ->   6.2832
# expected output ->  360

# input ->   0.7854
# expected output ->  45


import math
radians = float(input())
degrees = radians * 180 / math.pi

print(math.floor(degrees))
