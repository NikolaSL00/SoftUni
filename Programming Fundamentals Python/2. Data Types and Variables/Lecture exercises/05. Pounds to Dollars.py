# Write a program which converts British pounds to US dollars formatted to the 3rd decimal point.
# 1 British Pound = 1.31 Dollars.

# INPUT:
# 80

# EXPECTED OUTPUT:
# 104.800


# INPUT:
# 39

# EXPECTED OUTPUT:
# 51.090

british_pounds = float(input())
us_dollars = 1.31 * british_pounds
print(f"{us_dollars:.3f}")
