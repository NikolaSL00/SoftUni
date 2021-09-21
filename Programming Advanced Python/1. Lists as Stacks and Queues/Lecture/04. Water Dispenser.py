# Write a program which keeps track of people who are getting water from a dispenser
# and the amount of water left at the end.
# On the first line you will receive the starting quantity of water (integer) in a dispenser.
# Then, on the next few lines you will be given the names of some people who want to get water
# (each on separate line) until you receive the command "Start".
# Add those people in a queue. Finally, you will receive some commands until the command "End":
# "{liters}" - litters (integer) that the current person in the queue wants to get.
# Check if there is enough water in the dispenser for that person.
# If there is enough water, print "{person_name} got water" and remove him/her from the queue.
# Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water
# in the dispenser.
# "refill {liters}" - add the given litters in the dispenser.
# At the end print how many litters of water have left in the format: "{left_liters} liters left".

# Input:
# 2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End

# Expected Output:
# Peter got water
# Amy got water
# 0 liters left

# Input:
# 10
# Peter
# George
# Amy
# Alice
# Start
# 2
# 3
# 3
# 3
# End

# Expected Output:
# Peter got water
# George got water
# Amy got water
# Alice must wait
# 2 liters left

from collections import deque

litres_in_dispenser = int(input())

queue = deque()
name = input()

while name != "Start":
    queue.appendleft(name)
    name = input()

litres_or_refill_litres = ""

while queue or litres_or_refill_litres.startswith("End"):
    litres_or_refill_litres = input()

    if litres_or_refill_litres.startswith("refill"):
        litres = int(litres_or_refill_litres.split(" ")[1])
        litres_in_dispenser += litres
    else:
        litres = int(litres_or_refill_litres)

        if litres_in_dispenser - litres < 0:
            print(f"{queue.pop()} must wait")
        else:
            litres_in_dispenser -= litres
            print(f"{queue.pop()} got water")

print(f"{litres_in_dispenser} liters left")
