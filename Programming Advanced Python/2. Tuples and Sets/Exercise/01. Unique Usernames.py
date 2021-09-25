# Write a program that reads from the console a sequence of N usernames and keeps
# a collection only of the unique ones. On the first line, you will receive an integer N.
# On the next N lines, you will receive a username.
# Print the collection on the console (the order does not matter):

# INPUT:
# 6
# George
# George
# George
# Peter
# George
# NiceGuy1234

# OUTPUT:
# George
# Peter
# NiceGuy1234


# INPUT:
# 10
# Peter
# Maria
# Peter
# George
# Steve
# Maria
# Alex
# Peter
# Steve
# George

# OUTPUT:
# Peter
# Maria
# George
# Steve
# Alex

number_of_usernames = int(input())

usernames = {input() for _ in range(number_of_usernames)}

for username in usernames:
    print(username)
