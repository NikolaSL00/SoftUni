# Write a program that keeps information about students and their grades.
# You will receive n pair of rows. First you will receive the student's name, after that you will receive his grade. Check if the student already exists and if not, add him. Keep track of all grades for each student.
# When you finish reading the data, keep the students with average grade higher than or equal to 4.50. Order the filtered students by average grade in descending order.
# Print the students and their average grade in the following format:
# {name} -> {averageGrade}
# Format the average grade to the 2nd decimal place.

# INPUT:
# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5

# OUTPUT:
# John -> 5.00
# George -> 5.00
# Alice -> 4.50

# INPUT:
# 5
# Amanda
# 3.5
# Amanda
# 4
# Rob
# 5.5
# Christian
# 5
# Robert
# 6

# OUTPUT:
# Robert -> 6.00
# Rob -> 5.50
# Christian -> 5.00

n = int(input())

dictionary_with_students = {}

for _ in range(n):
    student_name = input()
    if student_name not in dictionary_with_students.keys():
        student_grade = float(input())
        dictionary_with_students[student_name] = list()
        dictionary_with_students[student_name].append(student_grade)
    else:
        student_grade = float(input())
        dictionary_with_students[student_name].append(student_grade)

dictionary_with_students_over_the_treshhold = {key: value for key, value in dictionary_with_students.items() if
                                               sum(value) / len(value) >= 4.50}

for student, grades in sorted(dictionary_with_students_over_the_treshhold.items(),
                              key=lambda kvp: -sum(kvp[1]) / len(kvp[1])):
    print(f"{student} -> {sum(grades) / len(grades):.2f}")
