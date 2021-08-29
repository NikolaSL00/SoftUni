# Да се напише програма, която чете 2*n-на брой цели числа,
# подадени от потребителя,
# и проверява дали сумата на първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума).
# При равенство печата " Yes, sum = " + сумата; иначе печата " No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).

# input:
# 2
# 10
# 90
# 60
# 40
# expected output:
# Yes, sum = 100

# input:
# 2
# 90
# 9
# 50
# 50
# expected output:
# No, diff = 1

count = int(input())
sum = 0
sum1 = 0
for n in range(0, count):
    number = int(input())
    sum += number
for n in range(0, count):
    number1 = int(input())
    sum1 += number1
if sum == sum1:
    print(f"Yes, sum = {sum}")
else:
    print(f"No, diff = {abs(sum - sum1)}")
