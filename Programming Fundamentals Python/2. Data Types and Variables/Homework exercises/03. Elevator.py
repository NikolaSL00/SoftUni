# Calculate how many courses will be needed to elevate n persons by using an elevator
# with capacity of p persons.
# The input holds two lines: the number of people n and the capacity p of the elevator.

# INPUT:
# 17
# 3

# EXPECTED OUTPUT:
# 6


# INPUT:
# 4
# 5

# EXPECTED OUTPUT:
# 1


n = int(input())
p = int(input())

counter = 0

while n > 0:
    n -= p
    counter += 1

print(counter)
