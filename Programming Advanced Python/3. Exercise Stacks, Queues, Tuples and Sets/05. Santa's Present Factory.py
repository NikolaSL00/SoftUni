# This year Santa has decided to share his secret with you. Get ready to learn how his dwarfs craft all the presents.
# First, you will receive a sequence of integers representing the number of materials for crafting toys in one box. After that, you will be given another sequence of integers – their magic level.
# Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic level:
#
#
# Present	Magic needed
# Doll	150
# Wooden train	250
# Teddy bear	300
# Bicycle 	400
#
# You should take the last box with materials and the first magic level value to craft a toy. Their multiplication calculates the total magic level. If the result equals one of the levels described in the table above, you craft the present and remove both materials and magic value. Otherwise:
# If the product of the operation is a negative number, you should sum the values together, remove them both from their positions, and add the result to the materials.
# If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the magic value and increase the material value by 15.
# If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
# Stop crafting presents when you run out of boxes of materials or magic level values.
# Your task is considered done if you manage to craft either one of the pairs:
# a doll and a train
# a teddy bear and a bicycle
# Input
# The first line of input will represent the values of boxes with materials - integers, separated by a single space
# On the second line, you will be given the magic values - integers again, separated by a single space
# Output
# On the first line - print whether you've succeeded in crafting the presents:
# "The presents are crafted! Merry Christmas!"
# "No presents this Christmas!"
# On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
# "Materials left: {material1}, {material2}, … {materialN}"
# "Magic left: {magicValue1}, {magicValue2}, … {magicValueN}"
# On the next lines print the presents you have crafted, ordered alphabetically in the format:
# "{toy_name1}: {amount}
# {toy_name2}: {amount}
# ...
# {toy_nameN}: {amount}"
# Constraints
# All the materials' values will be integers in the range [1, 100]
# Magic level values will be integers in the range [-10, 100]
# In all cases, at least one present will be crafted

# INPUT:
# 10 -5 20 15 -30 10
# 40 60 10 4 10 0

# OUTPUT:
# The presents are crafted! Merry Christmas!
# Materials left: 20, -5, 10
# Bicycle: 1
# Teddy bear: 2

# INPUT:
# 30 5 15 60 0 30
# -15 10 5 -15 25

# OUTPUT:
# No presents this Christmas!
# Materials left: 20, 30
# Doll: 1
# Teddy bear: 1

from collections import deque

crafted_presents = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

boxes = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

doll_and_a_train = crafted_presents["Doll"] > 0 and crafted_presents["Wooden train"] > 0
teddyBear_and_a_bicycle = crafted_presents["Teddy bear"] > 0 and crafted_presents["Bicycle"] > 0

while (not doll_and_a_train or not teddyBear_and_a_bicycle) and magic_values and boxes:
    current_box = boxes.pop()
    current_magic_value = magic_values.popleft()

    result = current_box * current_magic_value

    if result < 0:
        boxes.append(current_box + current_magic_value)

    elif result in presents:
        present = presents[result]

        if present in crafted_presents:
            crafted_presents[present] += 1
        else:
            crafted_presents[present] += 1
    elif result > 0:
        boxes.append(current_box + 15)
    else:
        if current_box != 0:
            boxes.append(current_box)
            continue
        elif current_magic_value != 0:
            magic_values.appendleft(current_magic_value)
            continue
        else:
            continue
    doll_and_a_train = crafted_presents["Doll"] > 0 and crafted_presents["Wooden train"] > 0
    teddyBear_and_a_bicycle = crafted_presents["Teddy bear"] > 0 and crafted_presents["Bicycle"] > 0

if doll_and_a_train or teddyBear_and_a_bicycle:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    boxes.reverse()
    print(f"Materials left: {', '.join(map(str, boxes))}")
if magic_values:
    print(f"Magic left: {', '.join(map(str, magic_values))}")

for toy, number in sorted(crafted_presents.items()):
    if number > 0:
        print(f"{toy}: {number}")
