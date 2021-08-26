# Първата задача от тази тема е да се напише конзолна програма, която чете оценка (реално число),
# въведена от потребителя и отпечатва "Excellent!", ако оценката е 5.50 или по-висока.

# input:    6
# expected output:  Excellent!

# input:    5
# expected output:  (няма изход)

# input:    5.50
# expected output:  Excellent!

grade = float(input())
if grade >= 5.50:
    print("Excellent!")