# Create a decorator function called even_parameters. It should check if all parameters passed to a function are even numbers and only then execute the function and return the result. Otherwise, don't execute the function and return "Please use only even numbers!"
import functools


def even_parameters(func):
    @functools.wraps(func)
    def wrapper(*args):
        # check if all are int numbers and if they are even
        # if yes run func
        # if no return message
        if all([isinstance(x, int) and x % 2 == 0 for x in args]):
            return func(*args)
        return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


# 6
# Please use only even numbers!


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
# 384
# Please use only even numbers!
