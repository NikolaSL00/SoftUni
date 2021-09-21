# Hot Potato is a game in which children form a circle and start tossing a hot potato.
# The counting starts with the first kid. Every nth toss the child who is holding the potato leaves the game.
# When a kid leaves the game, it passes the potato to the next kid. This continues until there is only one kid left.
# Create a program that simulates the game of Hot Potato. On the first line you will receive names of kids,
# separated by a single space. On the second line you will receive the nth toss (integer)
# in which a child leaves the game.
# Print every kid which is removed from the circle in the format "Removed {kid}".
# In the end, print the only kid left in the format "Last is {kid}".

# Input:
# Tracy Emily Daniel
# 2

# Expected Output:
# Removed Emily
# Removed Tracy
# Last is Daniel

# Input:
# George Peter Michael William Thomas
# 10

# Expected Output:
# Removed Thomas
# Removed Peter
# Removed Michael
# Removed George
# Last is William


# Input:
# George Peter Michael William Thomas
# 1

# Expected Output:
# Removed George
# Removed Peter
# Removed Michael
# Removed William
# Last is Thomas
from collections import deque

names = input().split(" ")
names_queue = deque(names)

step = int(input())

while names_queue:
    for i in range(step - 1):
        names_queue.append(names_queue.popleft())
    if len(names_queue) != 1:
        print(f"Removed {names_queue.popleft()}")
    else:
        print(f"Last is {names_queue.popleft()}")
