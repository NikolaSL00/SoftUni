# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N.
# On the following N lines, you will be receiving a student's name and their grade.
# For each student print all his/her grades and finally his/her average grade,
# formatted to the second decimal point in the format:
# "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.

# INPUT:
# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00

# OUTPUT:
# Mark -> 5.50 2.50 3.46 (avg: 3.82)
# Peter -> 5.20 3.20 (avg: 4.20)
# Alex -> 2.00 3.00 (avg: 2.50)


# INPUT:
# 4
# Scott 4.50
# Ted 3.00
# Scott 5.00
# Ted 3.66

# OUTPUT:
# Ted -> 3.00 3.66 (avg: 3.33)
# Scott -> 4.50 5.00 (avg: 4.75)


# INPUT:
# 5
# Lee 6.00
# Lee 5.50
# Lee 6.00
# Peter 4.40
# Kenny 3.30

# OUTPUT:
# Peter -> 4.40 (avg: 4.40)
# Lee -> 6.00 5.50 6.00 (avg: 5.83)
# Kenny -> 3.30 (avg: 3.30)

def avg(values):
    return sum(values) / len(values)


number_of_the_students = int(input())

dictionary_with_grades = {}

for _ in range(number_of_the_students):
    student_name, grade = input().split()
    grade = float(grade)

    if student_name not in dictionary_with_grades:
        dictionary_with_grades[student_name] = list()
    dictionary_with_grades[student_name].append(grade)

for student_name, grades in dictionary_with_grades.items():
    average_grade = avg(grades)
    grades_string = " ".join([str(f"{x:.2f}") for x in grades])
    print(f"{student_name} -> {grades_string} (avg: {average_grade:.2f})")
