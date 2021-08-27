# Напишете програма, която чете две цели числа (N1 и N2) и оператор,
# с който да се извърши дадена математическа операция. Възможните операции са: Събиране(+),
# Изваждане(-), Умножение(*),  Деление(/) и Модулно деление(%).
# При събиране, изваждане и умножение на конзолата трябва да се отпечатат резултата и дали той е четен или нечетен.
# При обикновеното деление - резултата. При модулното деление - остатъка.
# Трябва да се има предвид, че делителят може да е равен на 0 (нула), а на нула не се дели.
# В този случай трябва да се отпечата специално съобщениe.

# Вход
# От конзолата се прочитат 3 реда, въведени от потребителя:
# ⦁	N1 - цяло число;
# ⦁	N2 - цяло число;
# ⦁	Оператор - един символ измежду: "+", "-", "*", "/", "%".

# Изход
# Да се отпечата на конзолата един ред:
# ⦁	Ако операцията е събиране, изваждане или умножение:
# ⦁	 "{N1} {оператор} {N2} = {резултат} - {even/odd}"
# ⦁	Ако операцията е деление:
# ⦁	"{N1} / {N2} = {резултат}" - резултат, форматиран до втория знак след десетичната запетая
# ⦁	Ако операцията е модулно деление:
# ⦁	"{N1} % {N2} = {остатък}"
# ⦁	В случай на деление с 0 (нула):
# ⦁	"Cannot divide {N1} by zero"

# input:
# 10
# 12
# +
# expected output:
# 10 + 12 = 22 - even

# input:
# 10
# 1
# -
# expected output:
# 10 - 1 = 9 - odd

# input:
# 7
# 3
# *
# expected output:
# 7 * 3 = 21 - odd

first_number = int(input())
second_number = int(input())
operator = input()

result = 0
even_odd = "N/A"

if operator == "+":
    result = first_number + second_number
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{first_number} {operator} {second_number} = {result} - {even_odd}")
elif operator == "-":
    result = first_number - second_number
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{first_number} {operator} {second_number} = {result} - {even_odd}")
elif operator == "*":
    result = first_number * second_number
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{first_number} {operator} {second_number} = {result} - {even_odd}")
elif operator == "/":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.2f}")
elif operator == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result}")


