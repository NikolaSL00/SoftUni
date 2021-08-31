# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example 2018.
# Write a program that receives an integer number and finds the next happy year.

# INPUT:
# 8989

# EXPECTED OUTPUT:
# 9012


# INPUT:
# 1001

# EXPECTED OUTPUT:
# 1023

current_year = int(input())

while True:
    current_year += 1
    counter1 = len(str(current_year))
    counter2 = len(set(str(current_year)))
    if counter1 == counter2:
        print(current_year)
        break
