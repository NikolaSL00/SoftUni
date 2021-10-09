# You are provided with the following code:
#
# On the first several lines, until you receive the command "Search", you will receive on separate lines the number as text and the number as integer
# When you receive "Search" on the next several lines until you receive the command "Remove", you will be given the searched number as text and you need to print it on the console
# When you receive "Remove" on the next several lines until you receive "End" you will be given the searched number as text and you need to remove it from the dictionary
# At the end you need to print what is left from the dictionary
# There is some missing code in the solution and there are some errors that may occur. Complete the code so the following errors are handled:
# Passing non-integer type to the variable number
# Searching for a non-existent number
# Removing a non-existent number
# Print appropriate messages when an error has occurred. The messages should be:
# "The variable number must be an integer"
# "Number does not exist in dictionary" - for non-existing keys


# INPUT:
# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End

# OUTPUT:
# 1
# {'one': 1}

# INPUT:
# one
# two
# Search
# Remove
# End

# OUTPUT:
# The variable number must be an integer
# {}

# INPUT:
# one
# 1
# Search
# one
# Remove
# two
# End

# OUTPUT:
# 1
# Number does not exist in dictionary
# {'one': 1}

dictionary = dict()

line = input()

while line != "Search":
    b = 5

    try:
        value = int(input())
        dictionary[line] = value
    except ValueError:
        print("The variable number must be an integer")
    line = input()


line = input()

while line != "Remove":
    try:
        print(dictionary[line])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

line = input()

while line != "End":
    try:
        del dictionary[line]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(dictionary)
