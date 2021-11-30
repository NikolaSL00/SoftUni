# Create a class called Calculator that has the following static methods:
# add(*args) - sums all the arguments passed to the function and returns the result
# multiply(*args) - multiplies all the numbers and returns the result
# divide(*args) - divides all the numbers (starting from the first one) and returns the result
# subtract(*args) - subtracts all the numbers (starting from the first one) and returns the result


# Test Code:
# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))

# Desired Output:
# 19
# 30
# 50.0
# 70

class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for el in args:
            result *= el
        return result

    @staticmethod
    def divide(*args):
        res = args[0]
        for index in range(len(args) - 1):
            res /= args[index + 1]
        return res

    @staticmethod
    def subtract(*args):
        res = args[0]
        for index in range(len(args) - 1):
            res -= args[index + 1]
        return res

