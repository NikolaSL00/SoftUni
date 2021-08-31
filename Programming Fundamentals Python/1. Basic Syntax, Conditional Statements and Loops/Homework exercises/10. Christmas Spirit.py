# It is time to get in a Christmas mood. You need to decorate the house in time for the big event,
# but you have limited days to do so.
# You will receive allowed quantity for one type of decoration and days left until Christmas day
# to decorate the house.
# There are 4 types of decorations and each piece costs a price
# Ornament Set – 2$ a piece
# Tree Skirt – 5$ a piece
# Tree Garlands – 3$ a piece
# Tree Lights – 15$ a piece
# Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.
# Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.
# Every fifth day you buy Tree Lights quantity of times and increase your Christmas spirit by 17.
# If you have bought Tree Skirts and Tree Garlands at the same day you additionally increase your spirit by 30.
# Every tenth day you lose 20 spirit, because your cat ruins all tree decorations,
# and you should rebuild the tree and buy one piece of tree skirt, garlands, and lights.
# That is why you are forced to increase the allowed quantity with 2 at the beginning of every eleventh day.
# Also, if the last day is a tenth day the cat decides to demolish even more and ruins the Christmas turkey,
# and you lose additional 30 spirit.
# At the end you must print the total cost and the gained spirit.

# Input / Constraints
# The input will consist of exactly 2 lines:
# quantity – integer in range [1…100]
# days – integer in range [1…100]

# Output
# At the end print the total cost and the total gained spirit in the following format:
# "Total cost: {budget}"
# "Total spirit: {totalSpirit}"

# INPUT:
# 1
# 7

# EXPECTED OUTPUT:
# Total cost: 37
# Total spirit: 58


# INPUT:
# 3
# 20

# EXPECTED OUTPUT:
# Total cost: 558
# Total spirit: 156


quantity = int(input())
remaining_days = int(input())

is_the_last_day_tenth = False

total_sum = 0
total_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

for current_day in range(1, remaining_days + 1):
    is_the_last_day_tenth = False
    is_same_time_fifth_and_third_day = False

    if current_day % 11 == 0:
        quantity += 2

    if current_day % 2 == 0:
        total_sum += ornament_set_price * quantity
        total_spirit += 5

    if current_day % 3 == 0:
        is_same_time_fifth_and_third_day = True
        total_sum += tree_skirt_price * quantity + tree_garlands_price * quantity
        total_spirit += 13

    if current_day % 5 == 0:
        total_sum += tree_lights_price * quantity
        total_spirit += 17
        if is_same_time_fifth_and_third_day:
            total_spirit += 30

    if current_day % 10 == 0:
        is_the_last_day_tenth = True
        total_sum += tree_skirt_price + tree_garlands_price + tree_lights_price
        total_spirit -= 20

if is_the_last_day_tenth:
    total_spirit -= 30

print(f"Total cost: {total_sum}")
print(f"Total spirit: {total_spirit}")
