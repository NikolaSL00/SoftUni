# Да се напише програма, която чете n-на брой цели числа, подадени от потребителя,
# и проверява дали сумата от числата на четни позиции е равна на сумата на числата на нечетни позиции.
# При равенство да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата;
# иначе да се отпечата "No" и на нов ред "Diff = " + разликата.
# Разликата се изчислява по абсолютна стойност.

# input:
# 4
# 10
# 50
# 60
# 20
# expected output:
# Yes
# Sum = 70

# input:
# 4
# 3
# 5
# 1
# -2
# expected output:
# No
# Diff = 1

count = int(input())
even = 0
odd = 0
for n in range(0, count):
    number = int(input())
    if n % 2 == 0:
        even += number
    else:
        odd += number
if odd == even:
    print("Yes")
    print(f"Sum = {odd}")
else:
    print("No")
    print(f"Diff = {abs(odd - even)}")
