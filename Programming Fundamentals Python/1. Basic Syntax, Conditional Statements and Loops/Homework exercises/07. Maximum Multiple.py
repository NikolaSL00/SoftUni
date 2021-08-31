# On the first line you will be given a divisor, on the second line - a bound.
# The divisor and the bound are only positive integers. You should find the largest integer N, such that:
# N is divisible by the given divisor
# N is less than or equal to the given bound
# N is greater than 0
# Note: it is guaranteed that N is found.

# INPUT:
# 2
# 7

# EXPECTED OUTPUT:
# 6


# INPUT:
# 10
# 50

# EXPECTED OUTPUT:
# 50

divisor = int(input())
bound = int(input())

for n in range(bound, 0, -1):
    if n % divisor == 0:
        print(n)
        break
