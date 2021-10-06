# Create your own exception called ValueCannotBeNegative. Write a program that reads five numbers from the console (on separate lines). If a negative number occurs, raise the exception.

# INPUT:
# 1
# 4
# -5
# 3
# 10

# OUTPUT:
# Traceback (most recent call last):
#   File ".\value_cannot_be_negative.py", line 8, in <module>
#     raise ValueCannotBeNegative
# __main__.ValueCannotBeNegative

class ValueCannotBeNegative(Exception):
    pass


numbers = [int(input()) for _ in range(5)]
for number in numbers:
    if number < 0:
        raise ValueCannotBeNegative
