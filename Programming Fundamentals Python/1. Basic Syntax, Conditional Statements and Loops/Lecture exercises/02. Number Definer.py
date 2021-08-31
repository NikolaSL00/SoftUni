# Write a program that reads a floating-point number and prints "zero" if the number is zero.
# Otherwise, it should print "positive" or "negative".
# The program should add "small" if the absolute value of the number is less than 1,
# or "large" if it exceeds 1 000 000.

# INPUT:
# 25

# EXPECTED OUTPUT:
# positive

# INPUT:
# 435247392.921

# EXPECTED OUTPUT:
# large positive

# INPUT:
# -358583355123.001

# EXPECTED OUTPUT:
# large negative

number = float(input())

if number == 0:
    print("zero")
elif number < 0:
    if number > -1:
        print("small negative")
    elif number < -1000000:
        print("large negative")
    else:
        print("negative")
else:
    if number < 1:
        print("small positive")
    elif number > 1000000:
        print("large positive")
    else:
        print("positive")
