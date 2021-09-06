# You are at the shooting gallery again and you need a program that helps you keep track
# of moving targets. On the first line, you will receive a sequence of targets with their integer values,
# split by a single space. Then, you will start receiving commands for manipulating the targets,
# until the "End" command. The commands are the following:

# Shoot {index} {power}
# Shoot the target at the index, if it exists by reducing its value by the given power (integer value).A target is considered shot when its value reaches 0.
# Remove the target, if it is shot.

# Add {index} {value}
# Insert a target with the received value at the received index, if it exist. If not, print: "Invalid placement!"

# Strike {index} {radius}
# Remove the target at the given index and the ones before and after it depending on the radius, if such exist. If any of the indices in the range is invalid print:
# "Strike missed!" and skip this command.
#  Example:  Strike 2 2
# 	{radius}	{radius}	{strikeIndex}	{radius}	{radius}
#
# End
# Print the sequence with targets in the following format:
# {target1}|{target2}…|{targetn}
# Input / Constraints
# On the first line you will receive the sequence of targets – integer values [1-10000].
# On the next lines, until the "End" will be receiving the command described above – strings.
# There will never be a case when "Strike" command would empty the whole sequence.

# Output
# Print the appropriate message in case of "Strike" command if necessary.
# In the end, print the sequence of targets in the format described above.


# INPUT:
# 52 74 23 44 96 110
# Shoot 5 10
# Shoot 1 80
# Strike 2 1
# Add 22 3
# End

# EXPECTED OUTPUT:
# Invalid placement!
# 52|100

# INPUT:
# 47 55 85 78 99 20
# Shoot 1 55
# Shoot 8 15
# Strike 2 3
# Add 0 22
# Add 2 40
# Add 2 50
# End

# EXPECTED OUTPUT:
# Strike missed!
# 22|47|50|40|85|78|99|20

sequence_of_targets = [int(el) for el in input().split(" ")]

command = input()


def check_index(index: int, collection: list):
    if 0 <= index < len(collection):
        return True
    else:
        return False


while command != "End":
    not_end_command = command.split(" ")

    if not_end_command[0] == "Shoot":

        index = int(not_end_command[1])
        value = int(not_end_command[2])
        if check_index(index, sequence_of_targets):
            if sequence_of_targets[index] > value:
                sequence_of_targets[index] -= value
            else:
                sequence_of_targets.pop(index)

    elif not_end_command[0] == "Strike":
        index = int(not_end_command[1])
        radius = int(not_end_command[2])

        if check_index(index, sequence_of_targets):
            if check_index(index + radius, sequence_of_targets):
                if check_index(index - radius, sequence_of_targets):
                    for n in range(index + radius, index - radius - 1, -1):
                        sequence_of_targets.pop(n)
                else:
                    print("Strike missed!")
            else:
                print("Strike missed!")
        else:
            print("Strike missed!")

    elif not_end_command[0] == "Add":
        index = int(not_end_command[1])
        value = int(not_end_command[2])
        if check_index(index, sequence_of_targets):
            sequence_of_targets.insert(index, value)
        else:
            print("Invalid placement!")

    command = input()

print("|".join([str(el) for el in sequence_of_targets]))
