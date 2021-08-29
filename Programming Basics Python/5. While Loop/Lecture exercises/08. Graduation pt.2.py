# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение.
# На първия ред ще получите името на ученика, а на всеки следващ ред - неговите годишни оценки.
# Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00.
# Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата приключва,
# като се отпечатва името на ученика и в кой клас е изключен.

#  При успешно завършване на 12-ти клас да се отпечата :
# "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
# В случай, че ученикът е изключен от училище, да се отпечата:
# "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
# Стойността трябва да бъде форматирана до втория знак след десетичната запетая.

# input:
# Gosho
# 5
# 5.5
# 6
# 5.43
# 5.5
# 6
# 5.55
# 5
# 6
# 6
# 5.43
# 5
# expected output:
# Gosho graduated. Average grade: 5.53

# input:
# Mimi
# 5
# 6
# 5
# 6
# 5
# 6
# 6
# 2
# 3
# expected output:
# Mimi has been excluded at 8 grade

name = input()

avr_grade = 0.0
count = 0
count_under_4 = 0

while count < 12:
    grade = float(input())
    if grade >= 4.00:
        avr_grade += grade
    else:
        count_under_4 += 1
        if count_under_4 > 1:
            print(f"{name} has been excluded at {count} grade")
            break
        else:
            avr_grade += grade
    count += 1
else:
    avr_grade = avr_grade / 12
    print(f"{name} graduated. Average grade: {avr_grade:.2f}")
