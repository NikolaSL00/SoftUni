# Напишете програма, която чете n-на брой числа, въведени от потребителя, и пресмята сумата,
# минимума и максимума на числата на четни и нечетни позиции (броим от 1).
# Когато няма минимален / максимален елемент, отпечатайте "No".

# Изходът да се форматира в следния вид:
# "OddSum=" + {сума на числата на нечетни позиции},
# "OddMin=" + { минимална стойност на числата на нечетни позиции } / {"No"},
# "OddMax=" + { максимална стойност на числата на нечетни позиции } / {"No"},
# "EvenSum=" + { сума на числата на четни позиции },
# "EvenMin=" + { минимална стойност на числата на четни позиции } / {"No"},
# "EvenMax=" + { максимална стойност на числата на четни позиции } / {"No"}
# Всяко число трябва да е форматирано до втория знак след десетичната запетая.

# input:
# 6
# 2
# 3
# 5
# 4
# 2
# 1
# expected output:
# OddSum=9.00, OddMin=2.00, OddMax=5.00, EvenSum=8.00, EvenMin=1.00, EvenMax=4.00

# input:
# 2
# 1.5
# -2.5
# expected output:
# OddSum=1.50, OddMin=1.50, OddMax=1.50, EvenSum=-2.50, EvenMin=-2.50, EvenMax=-2.50

import sys

count = int(input())

even_sum_numbers = 0
even_max_number = -sys.maxsize
even_min_number = sys.maxsize

odd_sum_numbers = 0
odd_max_number = -sys.maxsize
odd_min_number = sys.maxsize

for n in range(1, count + 1):
    number = float(input())
    if n % 2 == 0:
        even_sum_numbers += number
        if number > even_max_number:
            even_max_number = number
        if number < even_min_number:
            even_min_number = number
    else:
        odd_sum_numbers += number
        if number > odd_max_number:
            odd_max_number = number
        if number < odd_min_number:
            odd_min_number = number

print(f"OddSum={odd_sum_numbers:.2f},")
if odd_min_number != sys.maxsize:
    print(f"OddMin={odd_min_number:.2f},")
else:
    print(f"OddMin=No,")
if odd_max_number != -sys.maxsize:
    print(f"OddMax={odd_max_number:.2f},")
else:
    print(f"OddMax=No,")
print(f"EvenSum={even_sum_numbers:.2f},")
if even_min_number != sys.maxsize:
    print(f"EvenMin={even_min_number:.2f},")
else:
    print(f"EvenMin=No,")
if even_max_number != -sys.maxsize:
    print(f"EvenMax={even_max_number:.2f}")
else:
    print(f"EvenMax=No")
