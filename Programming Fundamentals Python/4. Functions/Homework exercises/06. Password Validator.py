# Write a function that checks if a given password is valid. Password validations are:
# It should be 6 - 10 (inclusive) characters long
# It should consist only of letters and digits
# It should have at least 2 digits
# If a password is valid print "Password is valid".
# Otherwise, for every unfulfilled rule print a message:
# "Password must be between 6 and 10 characters"
# "Password must consist only of letters and digits"
# "Password must have at least 2 digits"


# INPUT:
# logIn

# EXPECTED OUTPUT:
# Password must be between 6 and 10 characters
# Password must have at least 2 digits


# INPUT:
# Pa$s$s

# EXPECTED OUTPUT:
# Password must consist only of letters and digits
# Password must have at least 2 digits


# INPUT:
# MyPass123

# EXPECTED OUTPUT:
# Password is valid

def check_is_password_valid(password):
    is_valid = True
    only_letters_and_digits = True
    digit_counter = 0
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    for i in range(0, len(password)):
        ascii_code = ord(password[i])
        if 48 <= ascii_code <= 57:
            digit_counter += 1
        elif ascii_code not in range(65, 91) and ascii_code not in range(97, 123):
            only_letters_and_digits = False
            is_valid = False
    if not only_letters_and_digits:
        print("Password must consist only of letters and digits")
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


password = input()

check_is_password_valid(password)
