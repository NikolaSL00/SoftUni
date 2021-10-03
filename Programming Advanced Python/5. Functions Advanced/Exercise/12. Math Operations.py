# Write a function named math_operations that receives a different number of integers as arguments and 4 keyword arguments. The keys will be single letters: "a", "s", "d", "m", and the values will be numbers.
# You need to take each integer argument from the sequence and do mathematical operations as follows:
# The first element should be added to the value of the key "a"
# The second element should be subtracted from the value of the key "s"
# The third element should be divisor to the value of the key "d"
# The fourth element should be multiplied by the value of the key "m"
# Each result should replace the value of the corresponding key
# You must repeat the same steps consecutively until you run out of numbers
# Beware: You cannot divide by 0. If the operation could throw an error, you should delete the element from the sequence and continue to the next operation.
# For more clarifications, see the examples below.
# Note: Submit only the function in the judge system
# Input
# There will be no input. Just parameters passed to your function.
# All of the given numbers will be valid integers in the range [-100, 100]
# Output
# The function should return the final dictionary

# Test Code:
# print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))

# OUTPUT:
# {'a': 9, 's': 15, 'd': -3.0, 'm': -45}

# Test Code:
# print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))

# OUTPUT:
# {'a': 5, 's': 2, 'd': 0.0, 'm': 0}

# Test Code:
# print(math_operations(6, a=0, s=0, d=0, m=0))

# OUTPUT:
# {'a': 6, 's': 0, 'd': 0, 'm': 0}
def if_in_range(range, tuple):
    return 0 <= range < len(tuple)


def math_operations(*args, **kwargs):
    index = 0
    while True:
        if if_in_range(index, args):
            if index % len(kwargs) == 0:
                kwargs["a"] = kwargs["a"] + args[index]
                index += 1
            elif index % len(kwargs) == 3:
                kwargs["m"] = kwargs["m"] * args[index]
                index += 1
            elif index % len(kwargs) == 1:
                kwargs["s"] = kwargs["s"] - args[index]
                index += 1
            elif index % len(kwargs) == 2:
                if args[index] == 0:
                    index += 1
                    continue
                kwargs["d"] = kwargs["d"] / args[index]
                index += 1
        else:
            break
    return kwargs

# print(math_operations(6, a=0, s=0, d=0, m=0))
# print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
# print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
