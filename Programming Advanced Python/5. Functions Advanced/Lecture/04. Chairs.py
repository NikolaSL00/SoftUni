# Write a program that receives names on the first line (separated by comma and space ", ") and a number of chairs on the second line (an integer). The chairs will always be less than the people. Find all the ways to fit those people on the chairs. Print each combination on a separate line.
# Note: In the example below, "Peter, George" is the same as "George, Peter", so we only print the first combination


# INPUT:
# Peter, George, Amy
# 2

# OUTPUT:
# Peter, George
# Peter, Amy
# George, Amy

# INPUT:
# Mariya, Emilly, Tom, Bob
# 1

# OUTPUT:
# Mariya
# Emilly
# Tom
# Bob


def generate_combinations(values, index, count, comb):
    if len(comb) == count:
        print(", ".join(comb))
        return
    for i in range(index, len(values)):
        comb.append(values[i])
        generate_combinations(values, i + 1, count, comb)
        comb.pop()


string = list(input().split(", "))
count = int(input())

generate_combinations(string, 0, count, [])
