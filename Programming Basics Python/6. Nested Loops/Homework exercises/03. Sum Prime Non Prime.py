# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop".
# Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа.
# Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости,
# ако на входа се подаде отрицателно число, да се изведе следното съобщение "Number is negative.".
# В този случай въведено число се игнорира и не се прибавя към нито една от двете суми,
# а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.

# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# "Sum of all prime numbers is: {prime numbers sum}"
# "Sum of all non prime numbers is: {nonprime numbers sum}"

# input:
# 3
# 9
# 0
# 7
# 19
# 4
# stop
# expected output:
# Sum of all prime numbers is: 29
# Sum of all non prime numbers is: 13

# input:
# 30
# 83
# 33
# -1
# 20
# stop
# expected output:
# Number is negative.
# Sum of all prime numbers is: 83
# Sum of all non prime numbers is: 83


number = input()

prime_sum = 0
not_prime_sum = 0
flag = False

while number != "stop":
    if int(number) < 0:
        print("Number is negative.")
        number = input()
        continue

    for n in range(2, int(number)):
        if int(number) % n == 0:
            not_prime_sum += int(number)
            flag = True
            break

    if not flag:
        prime_sum += int(number)
    flag = False

    number = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {not_prime_sum}")
