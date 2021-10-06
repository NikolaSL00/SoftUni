# Write a program that counts all characters in a string except for space (' ').
# Print all the occurrences in the following format:
# {char} -> {occurrences}

# INPUT:
# text

# OUTPUT:
# t -> 2
# e -> 1
# x -> 1

# INPUT:
# text text text

# OUTPUT:
# t -> 6
# e -> 3
# x -> 3

list_of_words = input().split()

dictionary = {}

for el in list_of_words:
    for char in el:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
for key, value in dictionary.items():
    print(f"{key} -> {value}")

