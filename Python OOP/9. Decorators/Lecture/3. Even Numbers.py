# Having the following code:
# @even_numbers
# def get_numbers(numbers):
#     return numbers
# print(get_numbers([1, 2, 3, 4, 5]))

# Output:
# [2, 4]

import functools


def even_numbers(function):
    @functools.wraps(function)
    def wrapper(*args):
        result = function(*args)
        return [el for el in result if el % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
