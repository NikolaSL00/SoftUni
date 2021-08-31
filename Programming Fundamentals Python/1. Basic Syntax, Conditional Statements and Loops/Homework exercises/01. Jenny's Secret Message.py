# Jenny studies programming with Python and wants to create a program that greets a user when he/she
# gives his/her name. The greeting should be in a format "Hello, {name}!".
# However, Jenny is in love with Johnny and would like to greet him differently: "Hello, my love!".
# Can you help her?

# INPUT:
# Peter

# EXPECTED OUTPUT:
# Hello, Peter!


# INPUT:
# Amy

# EXPECTED OUTPUT:
# Hello, Amy!


# INPUT:
# Johnny

# EXPECTED OUTPUT:
# Hello, my love!

name = input()

if name == "Johnny":
    print("Hello, my love!")
else:
    print(f"Hello, {name}!")
