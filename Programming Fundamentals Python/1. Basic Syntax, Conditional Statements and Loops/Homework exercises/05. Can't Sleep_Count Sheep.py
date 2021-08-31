# If you can't sleep, just count sheep! You will be given a positive integer, 3 for example.
# You should return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
# Input will always be valid, i.e. integers greater than 0.

# INPUT:
# 5

# EXPECTED OUTPUT:
# 1 sheep...2 sheep...3 sheep...4 sheep...5 sheep...


# INPUT:
# 1

# EXPECTED OUTPUT:
# 1 sheep...

number = int(input())

for i in range(1, number + 1):
    print(f"{i} sheep...", end="")
