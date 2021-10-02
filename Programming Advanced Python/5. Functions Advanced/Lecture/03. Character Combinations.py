# Write a program that reads a single string and prints all possible combinations of the characters in that string. Submit your solution in the judge system.

# INPUT:
# abc

# OUTPUT:
# 12


def permute(index, values):
    if index == len(values):
        print("".join(values))
        return

    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permute(index + 1, values)
        values[i], values[index] = values[index], values[i]


string = list(input())

permute(0, string)
