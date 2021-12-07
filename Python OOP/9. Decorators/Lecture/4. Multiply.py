# Having the following code:
# @multiply(3)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(3))

# Desired Output:
# 39

# Having the following code:
# @multiply(5)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(6))

# Desired Output:
# 80
import functools


def multiply(times):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)

            return result * times

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
