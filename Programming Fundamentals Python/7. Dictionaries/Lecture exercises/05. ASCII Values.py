# Write program that receives a list of characters separated by ", " and creates a dictionary with each character as a key and its ASCII value as a value. Try solving that problem using comprehensions.

# INPUT:
# a, b, c, a

# OUTPUT:
# {'a': 97, 'b': 98, 'c': 99}

# INPUT:
# d, c, m, h

# OUTPUT:
# {'d': 100, 'c': 99, 'm': 109, 'h': 104}

list_of_characters = input().split(", ")

dictionary = {el: ord(el) for el in list_of_characters}

print(dictionary)
