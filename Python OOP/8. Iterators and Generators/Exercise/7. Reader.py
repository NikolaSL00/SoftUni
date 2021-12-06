# Create a generator function called read_next() which should receive different number of arguments (all iterable). On each iteration it should return the next element from the current iterable, or the first element from the subsequent iterable.


# Test Code:
# for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
#     print(item, end='')

# Desired Output:
# string2dict

def read_next(*args):
    for arg in args:
        for el in arg:
            # if arg is dict:
            #     yield el.value()
            # else:
            yield el


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
