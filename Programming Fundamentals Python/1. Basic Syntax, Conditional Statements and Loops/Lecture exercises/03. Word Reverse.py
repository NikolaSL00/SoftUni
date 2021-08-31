# Write a program that receives a single word from a user, reverses it and prints it.


# INPUT:
# Python

# EXPECTED OUTPUT:
# nohtyP

# INPUT:
# banana

# EXPECTED OUTPUT:
# ananab

word = input()

reversed_word = ""

for num_char in range(len(word) - 1, -1, -1):
    reversed_word += word[num_char]

print(reversed_word)
