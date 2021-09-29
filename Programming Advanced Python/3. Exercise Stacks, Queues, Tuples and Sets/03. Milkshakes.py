# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start from the last chocolate and try to match it with the first cup of milk. If their values are equal, you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0, you should remove them from the records before mixing it with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to stop making chocolate milkshakes.

# Input
# On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
# On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".

# Output
# On the first line, print:
# If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
# Otherwise: "Not enough milkshakes."
# On the second line - print:
# If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
# Otherwise: "Chocolate: empty"
# On the third line - print:
# If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
# Otherwise: "Milk: empty"

# Constraints
# All given numbers will be valid integers in the range [-100 … 100].

# INPUT:
# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55

# OUTPUT:
# Great! You made all the chocolate milkshakes needed!
# Chocolate: 20
# Milk: 10, 55

# INPUT:
# -10, -2, -30, 10
# -5

# OUTPUT:
# Not enough milkshakes.
# Chocolate: -10, -2, -30, 10
# Milk: empty

# INPUT:
# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6

# OUTPUT:
# Great! You made all the chocolate milkshakes needed!
# Chocolate: empty
# Milk: 14, 6
from collections import deque

packets_with_chocolates_stack = [int(x) for x in input().split(", ")]
cups_of_milk_queue = deque([int(x) for x in input().split(", ")])

count_milkshakes = 0

while packets_with_chocolates_stack and cups_of_milk_queue and count_milkshakes != 5:

    current_chocolate = packets_with_chocolates_stack[-1]
    current_milk = cups_of_milk_queue[0]

    if current_milk <= 0 and current_chocolate <= 0:
        cups_of_milk_queue.popleft()
        packets_with_chocolates_stack.pop()
        continue

    if current_milk <= 0:
        cups_of_milk_queue.popleft()
        continue

    if current_chocolate <= 0:
        packets_with_chocolates_stack.pop()
        continue

    if current_milk == current_chocolate:
        packets_with_chocolates_stack.pop()
        cups_of_milk_queue.popleft()
        count_milkshakes += 1

    else:
        cups_of_milk_queue.append(cups_of_milk_queue.popleft())
        packets_with_chocolates_stack[-1] -= 5

if count_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if packets_with_chocolates_stack:
    print(f"Chocolate: {', '.join(map(str, packets_with_chocolates_stack))}")
else:
    print("Chocolate: empty")
if cups_of_milk_queue:
    print(f"Milk: {', '.join(map(str, cups_of_milk_queue))}")
else:
    print("Milk: empty")
