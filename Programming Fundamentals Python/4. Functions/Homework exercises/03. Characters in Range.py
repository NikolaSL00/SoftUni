# Write a function which receives two characters and returns a single string with all the characters
# in between them (according to the ASCII code), separated by a single space. Print the result on the console.

# INPUT:
# a
# d

# EXPECTED OUTPUT:
# b c


# INPUT:
# #
# :

# EXPECTED OUTPUT:
# $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9


def characters_between_them(ch_1, ch_2):
    ascii_1 = ord(ch_1)
    ascii_2 = ord(ch_2)
    for ch in range(ascii_1 + 1, ascii_2):
        print(chr(ch), end=" ")


char_1 = input()
char_2 = input()

characters_between_them(char_1, char_2)
