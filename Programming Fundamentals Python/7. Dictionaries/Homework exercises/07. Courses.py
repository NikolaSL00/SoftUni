# Write a program that keeps information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name, until you receive the command "end". Check if such course already exists, and if not, add the course. Register the user into the course. When you receive the command "end", print the courses with their names and total registered users, ordered by the count of registered users in descending order. For each contest print the registered users ordered by name in ascending order.
# Input
# Until the "end" command is received, you will be receiving input in the format: "{courseName} : {studentName}".
# The product data is always delimited by " : ".
# Output
# Print the information about each course in the following the format:
# "{courseName}: {registeredStudents}"
# Print the information about each student, in the following the format:
# "-- {studentName}"

# INPUT:
# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end

# OUTPUT:
# Programming Fundamentals: 2
# -- John Smith
# -- Linda Johnson
# JS Core: 1
# -- Will Wilson
# Java Advanced: 1
# -- Harrison White

# INPUT:
# Algorithms : Jay Moore
# Programming Basics : Martin Taylor
# Python Fundamentals : John Anderson
# Python Fundamentals : Andrew Robinson
# Algorithms : Bob Jackson
# Python Fundamentals : Clark Lewis
# end

# OUTPUT:
# Python Fundamentals: 3
# -- Andrew Robinson
# -- Clark Lewis
# -- John Anderson
# Algorithms: 2
# -- Bob Jackson
# -- Jay Moore
# Programming Basics: 1
# -- Martin Taylor

input_line = input()

dictionary_with_courses = {}

while input_line != "end":
    input_line = input_line.split(" : ")
    if input_line[0] not in dictionary_with_courses.keys():
        dictionary_with_courses[input_line[0]] = []
        dictionary_with_courses[input_line[0]].append(input_line[1])
    else:
        dictionary_with_courses[input_line[0]].append(input_line[1])

    input_line = input()

for course, list_of_students in sorted(dictionary_with_courses.items(), key=lambda kvp: -len(kvp[1])):
    print(f"{course}: {len(list_of_students)}")
    for el in sorted(list_of_students, key=lambda name: name):
        print(f"-- {el}")
