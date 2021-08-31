# Write a program which reads different floating-point numbers from the console.
# When it receives a number between 1 and 100 inclusive,
# the program should stop reading and should print "The number {number} is between 1 and 100".

# INPUT:
# -3
# 0.9
# 44

# EXPECTED OUTPUT:
# The number 44.0 is between 1 and 100


number = float(input())

while number < 1 or number > 100:
    number = float(input())
else:
    print(f"The number {number} is between 1 and 100")
