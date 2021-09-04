# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single line, separated by space,
# in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# "OutOfStock {gift}"
# Find the gifts with this name in your collection, if there are any, and change their values to "None".
# "Required {gift} {index}"
# Replace the value of the current gift on the given index with this gift if the index is valid.
# "JustInCase {gift}"
# Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None",
# separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"

# Input / Constraints
# On the 1st line you are going to receive the names of the gifts, separated by a single space.
# On the next lines, until the "No Money" command is received, you will be receiving commands.
# The input will always be valid.
# Index is valid when it is between 0 and length of the list – 1.

# Output
# Print the gifts in the format described above.

# INPUT:
# Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
# OutOfStock Eggs
# Required Spoon 2
# JustInCase ChocolateEgg
# No Money

# EXPECTED OUTPUT:
# StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg


# INPUT:
# Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes
# Required Paper 8
# OutOfStock Clothes
# Required Chocolate 2
# JustInCase Hat
# OutOfStock Cable
# No Money

# EXPECTED OUTPUT:
# Sweets Cozonac Chocolate Flowers Wine Eggs Hat

gifts_list = input().split(" ")

command_1 = "OutOfStock"
command_2 = "Required"
command_3 = "JustInCase"

command_end = "No Money"
command = input()

while command != command_end:
    list_of_command = command.split(" ")

    if list_of_command[0] == command_1:
        for gift in gifts_list:
            if gift == list_of_command[1]:
                index_of_el = gifts_list.index(gift)
                gifts_list[index_of_el] = "None"

    elif list_of_command[0] == command_2:
        if 0 <= int(list_of_command[2]) < len(gifts_list):
            gifts_list[int(list_of_command[2])] = list_of_command[1]

    elif list_of_command[0] == command_3:
        gifts_list[-1] = list_of_command[1]

    command = input()

for gift in gifts_list:
    if gift != "None":
        print(gift, end=" ")
