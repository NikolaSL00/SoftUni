# You will be receiving names of students, their ID and a course of programming they have taken in the format "{name}:{ID}:{course}". On the last line you will receive a name of a course in snake case lowercase letters. You should print only the information of the students taken the corresponding course in the format: "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique

# INPUT:
# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals

# OUTPUT:
# John - 5622
# Maya - 89
# Lilly - 633

# INPUT:
# Alex:6:programming basics
# Maria:7:programming basics
# Kaloyan:9:advanced
# Todor:10:fundamentals
# programming_basics

# OUTPUT:
# Alex - 6
# Maria - 7

data = input()
courses = {}

while ":" in data:
    student_name, student_id, course_name = data.split(":")

    if course_name not in courses:
        courses[course_name] = {}
    courses[course_name][student_id] = student_name
    data = input()

searched_course = data.split('_')
searched_course = " ".join(searched_course)
for key, value in courses.items():
    if key == searched_course:
        for key_1, value_1 in value.items():
            print(f"{value_1} - {key_1}")
