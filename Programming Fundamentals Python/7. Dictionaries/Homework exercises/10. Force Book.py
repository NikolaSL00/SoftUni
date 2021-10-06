# The force users are struggling to remember which side are the different forceUsers from, because they switch them too often. So you are tasked to create a web application to manage their profiles. You should store an information for every unique forceUser, registered in the application.
# You will receive several input lines in one of the following formats:
# {forceSide} | {forceUser}
# {forceUser} -> {forceSide}
# The forceUser and forceSide are strings, containing any character.
# If you receive forceSide | forceUser:
# If there is no such forceUser and no such forceSide -> create new forceSide and add the forceUser to the corresponding side.
# Only if there is no such forceUser in any forceSide -> add the forceUser to the corresponding side.
# If there is such forceUser already -> skip the command and continue to the next operation.
# If you receive a forceUser -> forceSide:
# If there is such forceUser already -> change his/her side.
# If there is no such forceUser in any forceSide -> add the forceUser to the corresponding forceSide.
# If there is no such forceUser and no such forceSide -> create new forceSide and add the forceUser to the corresponding side.
# Then you should print on the console: "{forceUser} joins the {forceSide} side!" .
# You should end your program when you receive the command "Lumpawaroo". At that point you should print each force side, ordered descending by forceUsers count, than ordered by name. For each side print the forceUsers, ordered by name.
# In case there are no forceUsers in a side, you shouldn`t print the side information.
# Input / Constraints
# The input comes in the form of commands in one of the formats specified above.
# The input ends, when you receive the command "Lumpawaroo".
# Output
# As output for each forceSide, ordered descending by forceUsers count, then by name,  you must print all the forceUsers, ordered by name alphabetically.
# The output format is:
# Side: {forceSide}, Members: {forceUsers.Count}
# ! {forceUser}
# ! {forceUser}
# ! {forceUser}
# In case there are NO forceUsers, don`t print this side.

# INPUT:
# Light | Gosho
# Dark | Pesho
# Lumpawaroo

# OUTPUT:
# Side: Dark, Members: 1
# ! Pesho
# Side: Light, Members: 1
# ! Gosho

# INPUT:
# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo

# OUTPUT:
# Ivan Ivanov joins the Lighter side!
# DCay joins the Lighter side!
# Side: Lighter, Members: 3
# ! DCay
# ! Ivan Ivanov
# ! Royal

def force_user_exists(force_dictionary: dict, member: str):
    for side, members in force_dictionary.items():
        if member in members:
            return side
    return ""


def initial_join_force_side(force_dictionary: dict, side: str, member: str):
    result = force_user_exists(force_dictionary, member)

    if result == "" and side not in force_dictionary.keys():
        force_dictionary[side] = list()
        force_dictionary[side].append(member)

    elif result == "":
        force_dictionary[side].append(member)


def remove_user_from_side(force_dictionary: dict, member: str):
    result = force_user_exists(force_dictionary, member)

    if result != "":
        force_dictionary[result].remove(member)


def change_force_side_command(force_dictionary: dict, side: str, member: str):
    if side not in force_dictionary and force_user_exists(force_dictionary, member) == "":
        force_dictionary[side] = list()
        force_dictionary[side].append(member)

    elif force_user_exists(force_dictionary, member) == "":
        force_dictionary[side].append(member)

    elif force_user_exists(force_dictionary, member) != "":
        remove_user_from_side(force_dictionary, member)
        if side not in force_dictionary:
            force_dictionary[side] = list()
            force_dictionary[side].append(member)
        else:
            force_dictionary[side].append(member)

    print(f"{member} joins the {side} side!")


command = input()

dictionary_with_users_and_sides = {}

while command != "Lumpawaroo":
    if "|" in command:
        side, member = command.split(" | ")

        initial_join_force_side(dictionary_with_users_and_sides, side, member)

    elif "->" in command:
        member, side = command.split(" -> ")
        change_force_side_command(dictionary_with_users_and_sides, side, member)

    command = input()

for side, members in sorted(dictionary_with_users_and_sides.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    if len(members) > 0:
        print(f"Side: {side}, Members: {len(members)}")

        for el in sorted(members):
            print(f"! {el}")
