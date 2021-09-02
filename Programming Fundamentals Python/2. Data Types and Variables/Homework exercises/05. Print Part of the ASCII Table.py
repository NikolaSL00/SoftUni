# Write a program which prints part of the ASCII table characters on the console,
# separated by a single space. On the first line of input, you will receive the char index you should start with.
# On the second line - the index of the last character you should print.

# INPUT:
# 60
# 65

# EXPECTED OUTPUT:
# < = > ? @ A


# INPUT:
# 40
# 55

# EXPECTED OUTPUT:
# ( ) * + , - . / 0 1 2 3 4 5 6 7


number = int(input())
number1 = int(input())

for n in range(number, number1 + 1):
    print(chr(n), end=" ")
