# You will receive a number representing the number of wagons a train has. Create a list (train)
# with the given length containing only zeros. Until you receive the command "End",
# you will receive some of the following commands:

# ⦁	"add {people}" – you should add the number of people in the last wagon
# ⦁	"insert {index} {people}" - you should add the number of people at the given wagon
# ⦁	"leave {index} {people}" - you should remove the number of people from the wagon
# After you receive the "End" command print the train.

# INPUT:
# 3
# add 20
# insert 0 15
# leave 0 5
# End

# EXPECTED OUTPUT:
# [10, 0, 20]


# INPUT:
# 5
# add 10
# add 20
# insert 0 16
# insert 1 44
# leave 1 12
# insert 2 100
# insert 4 61
# leave 4 1
# add 15
# End

# EXPECTED OUTPUT:
# [16, 32, 100, 0, 105]


size = int(input())
wagon = [0] * size

command = input()

while command != "End":
    command_list = command.split(" ")

    if command_list[0] == "add":
        wagon[-1] += int(command_list[1])
    elif command_list[0] == "insert":
        index = int(command_list[1])
        people = int(command_list[2])
        wagon[index] += people
    elif command_list[0] == "leave":
        index = int(command_list[1])
        people = int(command_list[2])
        wagon[index] -= people

    command = input()

print(wagon)
