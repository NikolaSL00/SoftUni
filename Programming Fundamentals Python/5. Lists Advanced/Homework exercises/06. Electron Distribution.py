# You are a mad scientist and you have decided to play with electron distribution among atom's shells.
# You know that basic idea of electron distribution is that electrons should fill a shell until it's holding
# the maximum number of electrons.
# You will receive a single integer – number of electrons.
# Your task is to fill shells until there are no more electrons left.
# The rules for electron distribution are as follows:
# The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1).
# For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.

# You should start filling the shells from the first one at the first position.
# If the electrons are enough to completely fill the first shell,
# the left unoccupied electrons should fill the next shell and so on.

# At the end, print a list with the filled shells.

# INPUT:
# 10

# EXPECTED OUTPUT:
# [2, 8]


# INPUT:
# 44

# EXPECTED OUTPUT:
# [2, 8, 18, 16]


number_of_electrons = int(input())

shell_list = []

while number_of_electrons > 0:
    element = 2 * (len(shell_list) + 1) ** 2
    if element <= number_of_electrons:
        shell_list.append(element)
        number_of_electrons -= element
    else:
        shell_list.append(number_of_electrons)
        number_of_electrons = 0

print(shell_list)
