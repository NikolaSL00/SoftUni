# You have a water tank with capacity of 255 liters.
# On the first line, you will receive n – the number of lines, which will follow.
# On the next n lines, you will receive liters of water (integers), which you should pour in your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line.
# On the last line, print the liters in the tank.

# INPUT:
# 5
# 20
# 100
# 100
# 100
# 20

# EXPECTED OUTPUT:
# Insufficient capacity!
# 240


# INPUT:
# 7
# 10
# 20
# 30
# 10
# 5
# 10
# 20

# EXPECTED OUTPUT:
# 105

number_of_lines = int(input())

liters_counter = 0
for n in range(0, number_of_lines):
    add_liters = int(input())
    if liters_counter + add_liters <= 255:
        liters_counter += add_liters
    else:
        print("Insufficient capacity!")
else:
    print(liters_counter)
