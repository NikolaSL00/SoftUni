# As a young traveler, you gather items and craft new items.
# You will receive a journal with some Collecting items, separated with ', ' (comma and space).
# After that, until receiving "Craft!" you will be receiving different commands.
# Commands (split by " - "):
# "Collect - {item}" – Receiving this command, you should add the given item in your inventory.
# If the item already exists, you should skip this line.
# "Drop - {item}" – You should remove the item from your inventory, if it exists.
# "Combine Items - {oldItem}:{newItem}" – You should check if the old item exists,
# if so, add the new item after the old one. Otherwise, ignore the command.
# "Renew – {item}" – If the given item exists, you should change its position and put it last in your inventory.

# Output
# After receiving "Craft!" print the items in your inventory, separated by ", " (comma and space).


# INPUT:
# Iron, Wood, Sword
# Collect - Gold
# Drop - Wood
# Craft!

# EXPECTED OUTPUT:
# Iron, Sword, Gold

# INPUT:
# Iron, Sword
# Drop - Bronze
# Combine Items - Sword:Bow
# Renew - Iron
# Craft!

# EXPECTED OUTPUT:
# Sword, Bow, Iron


journals_with_iteams = input().split(", ")

command = input()


def cmmd_collect(collection: list, iteam: str):
    if not iteam in collection:
        collection.append(iteam)


def cmmd_drop(collection: list, item: str):
    if item in collection:
        collection.remove(item)


def cmmd_renew(collection: list, item: str):
    if item in collection:
        cmmd_drop(collection, item)
        collection.append(item)


def cmmd_combine(collection: list, item: str):
    first_item, second_item = item.split(":")
    if first_item in collection:
        index = collection.index(first_item)
        collection.insert(index + 1, second_item)


while command != "Craft!":
    splitted_command = command.split(" - ")

    if splitted_command[0] == "Collect":
        cmmd_collect(journals_with_iteams, splitted_command[1])
    elif splitted_command[0] == "Drop":
        cmmd_drop(journals_with_iteams, splitted_command[1])
    elif splitted_command[0] == "Renew":
        cmmd_renew(journals_with_iteams, splitted_command[1])
    elif splitted_command[0] == "Combine Items":
        cmmd_combine(journals_with_iteams, splitted_command[1])

    command = input()

print(", ".join(journals_with_iteams))
