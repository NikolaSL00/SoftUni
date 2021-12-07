# Having the following code:
# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
# print(get_letters())

# Desired Output:
# ["a", "e"]
import functools


def is_vowel(ch):
    vowel_list = ['a', 'e', 'u', 'e', 'o']
    if ch in vowel_list:
        return True
    return False


def vowel_filter(function):
    @functools.wraps(function)
    def wrapper():
        result = function()
        res = [el for el in result if is_vowel(el.lower())]
        return res

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
