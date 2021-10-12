import math


def calculate_logarithm(x, base_as_str):
    if base_as_str == "Natural":
        return math.log(x)

    base = int(base_as_str)
    return math.log(x, base)


print(f"{calculate_logarithm(10, 10):.2f}")
print(f"{calculate_logarithm(1024, 2)}")
print(f"{calculate_logarithm(10, 'Natural')}")
