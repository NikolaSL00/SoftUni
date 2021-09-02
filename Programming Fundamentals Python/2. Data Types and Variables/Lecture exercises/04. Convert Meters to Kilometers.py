# You will be given an integer which represents a distance in meters.
# Write a program which converts meters to kilometers formatted to the second decimal point.

# INPUT:
# 1852

# EXPECTED OUTPUT:
# 1.85


# INPUT:
# 798

# EXPECTED OUTPUT:
# 0.80


meters = float(input())
kilometers = meters / 1000
print(f"{kilometers:.2f}")
