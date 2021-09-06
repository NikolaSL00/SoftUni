# Using a comprehension write a program that receives a text and removes all the vowels from it,
# case insensitive. Print the new text string after removing the vowels.
# The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

# INPUT:
# Python

# EXPECTED OUTPUT:
# Pythn


# INPUT:
# ILovePython

# EXPECTED OUTPUT:
# LvPythn


input_text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

result = [el for el in input_text if el.lower() not in vowels]

print("".join(result))
