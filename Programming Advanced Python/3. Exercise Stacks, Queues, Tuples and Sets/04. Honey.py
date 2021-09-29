# We think the process of making honey is amazing! Let's learn more about how bees make honey.
# Worker-bees collect nectar. When a worker-bee has found enough nectar, she returns to the hive to drop off the load. The worker-bees pass the nectar to waiting bees so they can really start the honey-making process.
# You will receive 3 sequences:
# a sequence of integers, representing working bees,
# a sequence of integers, representing nectar,
# a sequence of symbols – "+", "-", "*" or "/", representing the honey-making process.
# Your task is to check if the bee has collected enough nectar to return to the hive and to keep track of the total honey waiting bees have made with the collected nectar.
# Step one: you should check if the bee has collected enough nectar. You should take the first bee and try to match it with the last nectar:
# If the nectar value is more or equal to the value of the bee, it is considered collected, and the bee returns to the hive to drop off the load (step two).
# If the nectar value is less than the value of the bee, you should remove the nectar and try to match the bee with the next nectar's value.
# Step two: you should calculate the honey made with the passed nectar. When you find a bee and nectar that have matched (step one), you should take the first symbol in the sequence of symbols ("+", "-", "*" or "/") and make the corresponding calculation as follows:
# "{matched bee} {symbol} {matched nectar}"
# The result represents the honey that is made from the passed nectar. The calculation should always return the absolute value of the result. After the calculation, remove the bee, the nectar, and the symbol.
# Stop making honey when you are out of bees or nectar.
# Input
# On the first line, you will be given the values of bees - integers, separated by a single space
# On the second line, you will be given the nectar's values - integers, separated by a single space
# On the third line, you will be given symbols - "+", "-", "*" or "/", separated by a single space
# Output
# On the first line - print the total honey made:
# "Total honey made: {total honey}"
# On the next two lines print the bees or the nectar that are left, if there are any, otherwise skip the line:
# "Bees left: {bee1}, {bee2}, … {beeN}"
# "Nectar left: {nectar1}, {nectar2}, … {nectarN}"
# Constraints
# All the bee's values will be integers in the range [0, 150]
# Nectar's values will be integers in the range [0, 150]
# There always will be enough symbols in the sequence of symbols

# INPUT:
# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /

# OUTPUT:
# Total honey made: 148
# Bees left: 99, 35, 0, 150

# INPUT:
# 30
# 15 9 5 150 8
# * + + * -

# OUTPUT:
# Total honey made: 4500
# Nectar left: 15, 9, 5
from collections import deque

arithmetic_signs = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "/": lambda a, b: a / b,
    "*": lambda a, b: a * b
}

working_bees_queue = deque([int(x) for x in input().split()])
nectar_stack = [int(x) for x in input().split()]
signs_queue = deque([x for x in input().split()])

made_honey = 0

while working_bees_queue and nectar_stack:
    current_bee = working_bees_queue.popleft()
    current_nectar = nectar_stack.pop()

    if current_bee <= current_nectar:
        current_sign = signs_queue.popleft()
        if current_sign == "/" and current_nectar == 0:
            continue
        else:
            made_honey += abs(arithmetic_signs[current_sign](current_bee, current_nectar))

    elif current_nectar < current_bee:
        working_bees_queue.appendleft(current_bee)

print(f"Total honey made: {made_honey}")
if working_bees_queue:
    print(f"Bees left: {', '.join(map(str, working_bees_queue))}")
if nectar_stack:
    print(f"Nectar left: {', '.join(map(str, nectar_stack))}")
