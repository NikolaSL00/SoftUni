# Напишете програма, която отпечатва числата в диапазона [1…1000], които завършват на 7.

for number in range(0, 1000):
    if number % 10 == 7:
        print(number)