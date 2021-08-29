# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта.
# Той обаче не знае колко парчета могат да си вземат гостите от нея.
# Вашата задача е да напишете програма, която изчислява броя на парчетата,
# които гостите са взели преди тя да свърши.
# Ще получите размерите на тортата (широчина и дължина – цели числа и след това на всеки ред,
# до получаване на командата "STOP" или докато не свърши тортата, броят на парчетата,
# които гостите вземат от нея. Всяко парче торта е с размер 1х1 см.

# Да се отпечата на конзолата един от следните редове:
# ⦁	"{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# ⦁	"No more cake left! You need {брой недостигащи парчета} pieces more."

# input:
# 10
# 10
# 20
# 20
# 20
# 20
# 21
# expected output:
# No more cake left! You need 1 pieces more.

# input:
# 10
# 2
# 2
# 4
# 6
# STOP
# expected output:
# 8	pieces are left.

cake_length = int(input())
cake_width = int(input())

cake_size = cake_width * cake_length
command = input()
while command != "STOP":
    cake_size -= float(command)
    if cake_size <= 0:
        p = int(abs(cake_size))
        print(f"No more cake left! You need {p} pieces more.")
        break
    command = input()
else:
    p = int(cake_size)
    print(f"{p} pieces are left.")
