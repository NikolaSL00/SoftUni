# A palindrome is a number which reads the same backward as forward, such as 323 or 1001.
# Write a function which receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False.
# Print the result.

# INPUT:
# 123, 323, 421, 121

# EXPECTED OUTPUT:
# False
# True
# False
# True


# INPUT:
# 32, 2, 232, 1010

# EXPECTED OUTPUT:
# False
# True
# True
# False

def is_palindrome(list_of_numbers):
    for number in list_of_numbers:
        if len(number) % 2 == 0:
            flag = True
            for i in range(0, int(len(number) / 2)):
                if number[i] == number[(i * (-1)) - 1]:
                    pass
                else:
                    flag = False
            print(flag)
        else:
            flag = True
            for i in range(0, int((len(number) - 1) / 2)):
                if number[i] == number[(i * (-1)) - 1]:
                    pass
                else:
                    flag = False
            print(flag)


list_of_numbers = input().split(", ")

is_palindrome(list_of_numbers)
