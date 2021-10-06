# You've done all the work and the last thing left to accomplish is to own a legendary item. However, it's a tedious process and it requires quite a bit of farming. Anyway, you are not too pretentious - any legendary item will do. The possible items are:
# Shadowmourne - requires 250 Shards;
# Valanyr - requires 250 Fragments;
# Dragonwrath - requires 250 Motes;
# Shards, Fragments and Motes are the key materials and everything else is junk. You will be given lines of input, in the format:
# 2 motes 3 ores 15 stones
# Keep track of the key materials - the first one that reaches the 250 mark, wins the race. At that point you have to print that the corresponding legendary item is obtained. Then, print the remaining shards, fragments, motes, ordered by quantity in descending order, then by name in ascending order, each on a new line. Finally, print the collected junk items in alphabetical order.
# Input
# Each line comes in the following format: {quantity} {material} {quantity} {material} … {quantity} {material}
# Output
# On the first line, print the obtained item in the format: {Legendary item} obtained!
# On the next three lines, print the remaining key materials in descending order by quantity
# If two key materials have the same quantity, print them in alphabetical order
# On the final several lines, print the junk items in alphabetical order
# All materials are printed in format {material}: {quantity}
# The output should be lowercase, except for the first letter of the legendary

# INPUT:
# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards

# OUTPUT:
# Valanyr obtained!
# fragments: 5
# shards: 5
# motes: 3
# leathers: 6
# stones: 5

# INPUT:
# 123 silver 6 shards 8 shards 5 motes
# 9 fangs 75 motes 103 MOTES 8 Shards
# 86 Motes 7 stones 19 silver

# OUTPUT:
# Dragonwrath obtained!
# shards: 22
# motes: 19
# fragments: 0
# fangs: 9
# silver: 123


def collect_materials(material: str, quantity: int, collection_junk: dict, collection: dict):
    if material not in collection.keys():
        if material not in collection_junk.keys():
            collection_junk[material] = quantity
        else:
            collection_junk[material] += quantity
    else:
        collection[material] += quantity


dict_of_items = {"fragments": 0, "motes": 0, "shards": 0}
junk = {}
item_obtained = ""

while item_obtained == "":
    list_of_items = input().split(" ")
    for index in range(len(list_of_items)):
        if index % 2 != 0:
            key = list_of_items[index].lower()
            collect_materials(key, value, junk, dict_of_items)
        else:
            value = int(list_of_items[index])

        if dict_of_items["shards"] >= 250:
            dict_of_items["shards"] -= 250
            item_obtained = "shards"
            print("Shadowmourne obtained!")
            break

        if dict_of_items["fragments"] >= 250:
            dict_of_items["fragments"] -= 250
            item_obtained = "fragments"
            print("Valanyr obtained!")
            break

        if dict_of_items["motes"] >= 250:
            dict_of_items["motes"] -= 250
            item_obtained = "motes"
            print("Dragonwrath obtained!")
            break

sorted_dict = sorted(dict_of_items.items(), key=lambda x: x[1], reverse=True)

for name, quantity in sorted_dict:
    if name == "motes" or name == "fragments" or name == "shards":
        print(f"{name}: {quantity}")

sorted_junk = sorted(junk.items(), key=lambda x: x[0], reverse=False)

for name, quantity in sorted_junk:
    if name != "motes" and name != "fragments" and name != "shards":
        print(f"{name}: {quantity}")
