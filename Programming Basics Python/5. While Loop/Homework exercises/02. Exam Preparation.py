# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни
# при команда "Enough" или ако Марин получи определения брой незадоволителни оценки.
# Незадоволителна е всяка оценка, която е по-малка или равна на 4.

# Вход
# ⦁	На първи ред - брой незадоволителни оценки - цяло число;
# ⦁	След това многократно се четат по два реда:
# ⦁	Име на задача – текст;
# ⦁	Оценка - цяло число в интервала [2…6].

# Изход
# ⦁	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# ⦁	"Average score: {средна оценка}"
# ⦁	"Number of problems: {броя на всички задачи}"
# ⦁	"Last problem: {името на последната задача}"
# ⦁	Ако получи определеният брой незадоволителни оценки:
# ⦁	"You need a break, {брой незадоволителни оценки} poor grades."

# Средната оценка да бъде форматирана до втория знак след десетичната запетая.

# input:
# 3
# Money
# 6
# Story
# 4
# Spring Time
# 5
# Bus
# 6
# Enough
# expected output:
# Average score: 5.25
# Number of problems: 4
# Last problem: Bus

# input:
# 2
# Income
# 3
# Game Info
# 6
# Best Player
# 4
# expected output:
# You need a break, 2 poor grades.

number_legal_weak_grades = int(input())
number_weak_grades = 0

problem = input()
grade = int(input())

last_problem = ""
avr_grade = 0
number_of_problems = 1

while problem != "Enough":
    if grade > 4:
        avr_grade += grade
    else:
        number_weak_grades += 1
        if number_weak_grades == number_legal_weak_grades:
            print(f"You need a break, {number_weak_grades} poor grades.")
            break
        else:
            avr_grade += grade
    problem = input()
    if problem != "Enough":
        last_problem = problem
        grade = int(input())
        number_of_problems += 1
else:
    avr_grade = avr_grade / number_of_problems
    print(f"Average score: {avr_grade:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")
