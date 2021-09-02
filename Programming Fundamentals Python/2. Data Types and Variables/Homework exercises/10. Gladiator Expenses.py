# As a gladiator, Peter needs to repair his broken equipment when he loses a fight.
# His equipment consists of helmet, sword, shield and armor. You will receive the Peter`s lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also brakes.
# Every second time, when his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment.
# Calculate his expenses for the year for renewing his equipment.

# Input / Constraints
# The input will consist of 5 lines:
# ⦁	On the first line you will receive the lost fights count – integer in the range [0, 1000].
# ⦁	On the second line you will receive the helmet price - floating point number in range [0, 1000].
# ⦁	On the third line you will receive the sword price - floating point number in range [0, 1000].
# ⦁	On the fourth line you will receive the shield price - floating point number in range [0, 1000].
# ⦁	On the fifth line you will receive the armor price - floating point number in range [0, 1000].

# Output
# ⦁	As output you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"

# INPUT:
# 7
# 2
# 3
# 4
# 5

# EXPECTED OUTPUT:
# Gladiator expenses: 16.00 aureus


# INPUT:
# 23
# 12.50
# 21.50
# 40
# 200

# EXPECTED OUTPUT:
# Gladiator expenses: 608.00 aureus


lost_fight_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
price = 0
for n in range(1, lost_fight_count + 1):
    if n % 2 == 0:
        price += helmet_price
    if n % 3 == 0:
        price += sword_price
    if n % 6 == 0:
        price += shield_price
    if n % 12 == 0:
        price += armor_price

print(f"Gladiator expenses: {price:.2f} aureus")
