# Create a decorator called cache. It should store all the returned values of the recursive function fibonacci. You are provided with this code:
#
# You need to create a dictionary called log that will store all the n's (keys) and the returned results (values) and attach that dictionary to the fibonacci function as a variable called log, so when you call it, it returns that dictionary. For more clarification, see the examples
import functools


def cache(func):
    log = {}

    @functools.wraps(func)
    def wrapper(num):
        if num not in log.keys():
            res = func(num)
            log[num] = res
            return res

        return log[num]

    wrapper.log = log
    return wrapper


@cache
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)
