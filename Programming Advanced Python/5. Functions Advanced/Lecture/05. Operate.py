# Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple numbers (integers) as additional arguments (*args). The function should return the result of the operator applied to all the numbers. For more clarification, see the examples below.
# Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division

# INPUT:
# print(operate("+", 1, 2, 3))

# OUTPUT:
# 6

# INPUT:
# print(operate("*", 3, 4))

# OUTPUT:
# 12

def operate(operator, *args):
    if operator == "*":
        res = 1
        for el in args:
            res *= el
        return res
    elif operator == "+":
        return sum(args)
    elif operator == "-":
        res = args[0]
        for index in range(1, len(args)):
            res -= args[index]
        return res
    elif operator == "/":
        res = args[0]
        for index in range(1, len(args)):
            res /= args[index]
        return res

# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))