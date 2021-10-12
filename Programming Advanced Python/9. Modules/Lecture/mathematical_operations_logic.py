import math


def perform_operation(number1, number2, operation):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        if number2 == 0:
            raise ValueError("Number2 must not be equal to 0. Can't devide by zero!")
        return number1 / number2
    elif operation == "^":
        return math.pow(number1, number2)
    else:
        raise ValueError("The operation must be one of the following: +, -, *, /, ^\n")
