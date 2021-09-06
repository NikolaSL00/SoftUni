# You will receive two lines of input:
# ⦁	a list of employees' happiness as string of numbers separated by a single space
# ⦁	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# You should increase their happiness by multiplying each of the employees' happiness by the factor.
# Then, print one of the following lines:

# ⦁	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# ⦁	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"


# INPUT:
# 1 2 3 4 2 1
# 3

# EXPECTED OUTPUT:
# Score 2/6. Employees are not happy!


# INPUT:
# 2 3 2 1 3 3
# 4

# EXPECTED OUTPUT:
# Score: 3/6. Employees are happy!

employees_happiness = [int(el) for el in input().split(" ")]
happiness_improvement_factor = int(input())

employees_happiness = [el * happiness_improvement_factor for el in employees_happiness]

average_happiness = sum(employees_happiness) / len(employees_happiness)

happy_employees = [el for el in employees_happiness if el >= average_happiness]

if len(happy_employees) >= len(employees_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")
