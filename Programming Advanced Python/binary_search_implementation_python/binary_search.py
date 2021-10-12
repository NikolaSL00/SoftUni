'''
[1,2,3,6,8,9,22,44,46,48,51,53,57,59,89,123,145,161,167,176,181,192]
# the list must be sorted
'''

# better implementation (faster)
import datetime


def binary_search(values, target, start_index, end_index):
    if start_index >= end_index:
        raise ValueError(f"{target} not in list")
    mid = (start_index + end_index) // 2
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        return binary_search(values, target, mid + 1, end_index)
    else:
        return binary_search(values, target, start_index, mid)


# slow implementation
def binary_search2(values, target):
    if not values:
        raise ValueError(f"{target} not in list.")

    mid = len(values) // 2
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        return mid + 1 + binary_search2(values[mid + 1:], target)
    else:
        return binary_search2(values[:mid], target)


def measure(action, repeat_count=1):
    dt_started = datetime.datetime.utcnow()
    for i in range(repeat_count):
        action()
    dt_ended = datetime.datetime.utcnow()

    print(f" --Executed in {(dt_ended - dt_started).total_seconds()} seconds")


def find_all(values):
    s = 0
    for val in values:
        s += binary_search(values, val, 0, len(values))
    return s


def find_all2(values):
    s = 0
    for val in values:
        s += binary_search2(values, val)
    return s


values = [x for x in range(2 ** 16)]

measure(lambda: find_all(values))
measure(lambda: find_all2(values))

# for val in values:
#     print(f" value = {val}, index = {binary_search2(values, val)}")
#
# print()
# print("________________________________________________")
# print()
#
# for val in values:
#     print(f" value = {val}, index = {binary_search(values, val, 0, len(values))}")
