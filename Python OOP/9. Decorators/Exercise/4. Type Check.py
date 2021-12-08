# Create a decorator called type_check. It should receive a type (int/float/str/…), and it should check if the parameter passed to the decorated function is of the type given to the decorator. If it is, execute the function and return the result, otherwise return "Bad Type".
import functools


def type_check(type):
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args):
            if all([isinstance(x, type) for x in args]):
                return func(*args)
            return 'Bad Type'

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))  # 4
print(times2('Not A Number'))  # Bad Type


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))  # H
print(first_letter(['Not', 'A', 'String']))  # Bad Type
