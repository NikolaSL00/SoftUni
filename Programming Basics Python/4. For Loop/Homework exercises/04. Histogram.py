# Дадени са n цели числа в интервала [1…1000].
# От тях някакъв процент p1 са под 200, друг процент p2 са от 200 до 399,
# друг процент p3 са от 400 до 599, друг процент p4 са от 600 до 799 и останалите p5 процента са от 800 нагоре.
# Да се напише програма, която изчислява и отпечатва процентите p1, p2, p3, p4 и p5.

# Пример: имаме n = 20 числа: 53, 7, 56, 180, 450, 920, 12, 7, 150, 250, 680, 2, 600, 200, 800, 799, 199, 46, 128, 65. Получаваме следното разпределение и визуализация:
# Диапазон	Числа в диапазона	                                Брой числа	Процент
# < 200	    53, 7, 56, 180, 12, 7, 150, 2, 199, 46, 128, 65	    12	        p1 = 12 / 20 * 100 = 60.00%
# 200 …     399	250, 200	                                    2	p2 = 2 / 20 * 100 = 10.00%
# 400 …     599	450	                                            1	p3 = 1 / 20 * 100 = 5.00%
# 600 …     799	680, 600, 799	                                3	p4 = 3 / 20 * 100 = 15.00%
# ≥ 800	920, 800	                                            2	p5 = 2 / 20 * 100 = 10.00%

# Вход
# На първия ред от входа стои цялото число n (1 ≤ n ≤ 1000) – брой числа. На следващите n реда стои по едно цяло число в интервала [1…1000] – числата върху които да бъде изчислена хистограмата.
# Изход
# Да се отпечата на конзолата хистограмата – 5 реда, всеки от които съдържа число между 0% и 100%, с точност две цифри след десетичната точка, например 25.00%, 66.67%, 57.14%.

# input:
# 3
# 1
# 2
# 999
# expected output:
# 66.67%
# 0.00%
# 0.00%
# 0.00%
# 33.33%

# input:
# 4
# 53
# 7
# 56
# 999
# expected output:
# 75.00%
# 0.00%
# 0.00%
# 0.00%
# 25.00%

n = int(input())

interval_0_199_count = 0
interval_200_399_count = 0
interval_400_599_count = 0
interval_600_799_count = 0
interval_800_1000_count = 0

for i in range(0, n):
    number = int(input())
    if 0 < number < 200:
        interval_0_199_count += 1
    elif 200 <= number < 400:
        interval_200_399_count += 1
    elif 400 <= number < 600:
        interval_400_599_count += 1
    elif 600 <= number < 800:
        interval_600_799_count += 1
    else:
        interval_800_1000_count += 1

p1 = interval_0_199_count / n * 100
p2 = interval_200_399_count / n * 100
p3 = interval_400_599_count / n * 100
p4 = interval_600_799_count / n * 100
p5 = interval_800_1000_count / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")