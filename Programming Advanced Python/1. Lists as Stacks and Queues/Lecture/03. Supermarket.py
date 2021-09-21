# Tom is working at the supermarket, and he needs your help to keep track of his clients.
# Write a program which reads lines of input consisting of a customer's name and adds it
# to the end of a queue until "End" is received. If in a meantime you receive the command "Paid",
# you should print each customer in the order they are served (from the first to the last one) and empty the queue.
# When you receive "End", you should print the count of the remaining people in the queue in the format:
# "{count} people remaining.".

# Input:
# George
# Peter
# William
# Paid
# Michael
# Oscar
# Olivia
# Linda
# End

# Expected Output:
# George
# Peter
# William
# 4 people remaining.

# Input:
# Anna
# Emma
# Alexander
# End

# Expected Output:
# 3 people remaining.

from collections import deque

queue = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif command == "Paid":
        while queue:
            print(queue.pop())
    else:
        queue.appendleft(command)
