# Create a decorator called logged. It should return the name of the function that is being called and its parameters. It should also return the result of the execution of the function being called. See the examples for more clarification.

# Test Code:
# @logged
# def func(*args):
#     return 3 + len(args)
# print(func(4, 4, 4))

# Desired Output:
# you called func(4, 4, 4)
# it returned 6

# Test Code:
# @logged
# def sum_func(a, b):
#     return a + b
# print(sum_func(1, 4))

# Desired Output:
# you called sum_func(1, 4)
# it returned 5
import functools


def logged(func):
    @functools.wraps(func)
    def wrapper(*args):
        func_name = func.__name__
        result = func(*args)
        return f'you called {func_name}{args}\nit returned {result}'

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
