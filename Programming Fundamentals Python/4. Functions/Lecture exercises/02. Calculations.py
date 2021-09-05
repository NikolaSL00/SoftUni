# Create a function which receives three parameters, calculates a result depending on the given operator
# and returns it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following:  'multiply', 'divide', 'add', 'subtract'.

# INPUT:
# subtract
# 5
# 4

# EXPECTED OUTPUT:
# 1


# INPUT:
# divide
# 8
# 4

# EXPECTED OUTPUT:
# 2


def operation(operator, num_1, num_2):
    if operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return num_1 // num_2
    elif operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2


oper = input()
number_1 = int(input())
number_2 = int(input())
result = operation(oper, number_1, number_2)
print(result)
