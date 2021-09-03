# The group of adventurists have gone on their first task. Now they should walk through fire - literally. They should use all the water they have left. Your task is to help them survive.
# Create a program that calculates the water that is needed to put out a "fire cell", based on the given information about its "fire level" and how much it gets affected by water.
# First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the needed water to put out the fire.  They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}……"
# Afterwards you will receive the amount of water you have for putting out the fires. There is a range of fire for each of the fire types, and if a cell’s value is below or exceeds it, it is invalid, and you do not need to put it out.
# Type of Fire	Range
# High	81 - 125
# Medium	51 - 80
# Low	1 - 50
# If a cell is valid, you should put it out by reducing the water with its value. Putting out fire also takes effort, and you need to calculate it. Its value is equal to 25% of the cell’s value. In the end you will have to print the total effort. Keep putting out cells until you run out of water. If you do not have enough water to put out a given cell – skip it and try the next one. In the end, print the cells you have put out in the following format:
# "Cells:
#  - {cell1}
#  - {cell2}
#  - {cell3}
# ……
#  - {cellN}"
# "Effort: {effort}"
# In the end, print the total fire you have put out from all of the cells in the following format: "Total Fire: {totalFire}"
# Input / Constraints
# On the 1st line you are going to receive the fires with their cells in the format described above – integer numbers in the range [1…500]
# On the 2nd line, you are going to be given the water – an integer number in the range [0….100000]
# Output
# Print the cells, which you have put out in the following format:
# "Cells:
#  - {cell}
#  - {cell2}
#  - {cell3}
#  - {cell5}
# ……
#  - {cellN}"
# Print the effort, rounded 2 digits after the decimal separator in the following format:
# "Effort: {effort}"
# Print the total fire put out
# "Total Fire: {totalFire}"


# INPUT:
# High = 89#Low = 28#Medium = 77#Low = 23
# 1250

# EXPECTED OUTPUT:
# Cells:
#  - 89
#  - 28
#  - 77
#  - 23
# Effort: 54.25
# Total Fire: 217


# INPUT:
# High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77
# 220

# EXPECTED OUTPUT:
# Cells:
#  - 40
#  - 110
# Effort: 37.50
# Total Fire: 150

level_of_fire_in_cells_halved_splitted = input().split("#")
water_amount = int(input())
effort_level = 0

level_of_fire_in_cells_fully_splitted = []
for element in level_of_fire_in_cells_halved_splitted:
    l = str(element)
    level_of_fire_in_cells_fully_splitted.append(l.split(" = "))

list_with_validated_cells_of_fire = []
for fire in level_of_fire_in_cells_fully_splitted:
    if fire[0] == "High":
        if 81 <= int(fire[1]) <= 125:
            list_with_validated_cells_of_fire.append(fire)
    if fire[0] == "Medium":
        if 51 <= int(fire[1]) <= 80:
            list_with_validated_cells_of_fire.append(fire)
    if fire[0] == "Low":
        if 1 <= int(fire[1]) <= 50:
            list_with_validated_cells_of_fire.append(fire)

putted_out_cells = []
for fire in list_with_validated_cells_of_fire:
    if water_amount >= int(fire[1]):
        water_amount -= int(fire[1])
        effort_level += 0.25 * int(fire[1])
        putted_out_cells.append(fire)
    else:
        continue
print("Cells:")
sum_of_putted_out_fire = 0
for fire in putted_out_cells:
    print(f" - {fire[1]}")
    sum_of_putted_out_fire += int(fire[1])
print(f"Effort: {effort_level:.2f}")
print(f"Total Fire: {sum_of_putted_out_fire}")
