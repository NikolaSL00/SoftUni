# Курсът "Train the trainers" е към края си и финалното оценяване наближава. Вашата задача е да помогнете на журито, което ще оценява презентациите, като напишете програма, в която да изчислява средната оценка от представянето на всяка една презентация от даден студент, а накрая - средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата
# "Student's final assessment is {среден успех от всички презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.

# input:
# 2
# While-Loop
# 6.00
# 5.50
# For-Loop
# 5.84
# 5.66
# Finish
# expected output:
# While-Loop - 5.75.
# For-Loop - 5.75.
# Student's final assessment is 5.75.

# input:
# 3
# Arrays
# 4.53
# 5.23
# 5.00
# Lists
# 5.83
# 6.00
# 5.42
# Finish
# expected output:
# Arrays - 4.92.
# Lists - 5.75.
# Student's final assessment is 5.34.


jury_members = int(input())
presentation_name = input()

average_grade_all = 0
average_grade = 0
grade = 0
counter = 0
while presentation_name != "Finish":
    counter += 1
    for n in range(0, jury_members):
        grade = float(input())
        average_grade += grade
    average_grade = average_grade / jury_members
    print(f"{presentation_name} - {average_grade:.2f}.")
    average_grade_all += average_grade
    average_grade = 0
    presentation_name = input()
print(f"Student's final assessment is {average_grade_all / counter:.2f}.")
