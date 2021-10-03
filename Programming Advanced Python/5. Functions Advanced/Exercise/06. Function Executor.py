# Create a function called func_executor() that can receive a different number of tuples, each of which will have exactly 2 elements: first will be a function, and the second will be a tuple of the arguments that need to be passed to that function. Create a list that will contain all the results of the executed functions with their corresponding arguments and return it after executing all functions. For more clarification, see the examples below. Submit only your function in the judge system.

# Test Code:
# def sum_numbers(num1, num2):
#     return num1 + num2
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
# print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

# OUTPUT:
# [3, 8]

def func_executor(*args):
    results = []
    for func, func_args in args:
        results.append(func(*func_args))
    return results


