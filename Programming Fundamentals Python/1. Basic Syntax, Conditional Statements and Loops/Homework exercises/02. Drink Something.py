# Kids drink toddy, teens drink coke, young adults drink beer, adults drink whisky.
# Create a program which receives an age and prints what they drink.

# Rules:
# Kid is defined as someone under the age of 14.
# Teen is defined as someone under the age of 18.
# Young adult is defined as someone under the age of 21.
# Adult is defined as someone above the age of 21.

# Note: All the values are inclusive except the last one!

# INPUT:
# 13

# EXPECTED OUTPUT:
# drink toddy


# INPUT:
# 17

# EXPECTED OUTPUT:
# drink coke


# INPUT:
# 30

# EXPECTED OUTPUT:
# drink whisky

age = int(input())

if age <= 14:
    print("drink toddy")
elif age <= 18:
    print("drink coke")
elif age <= 21:
    print("drink beer")
elif age > 21:
    print("drink whisky")
