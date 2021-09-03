# As a young baker, you are baking the bread out of the bakery.
# You have initial energy 100 and initial coins 100. You will be given a string, representing the working day events. Each event is separated with '|' (vertical bar): "event1|event2|event3…"
# Each event contains event name or item and a number, separated by dash("{event/ingredient}-{number}")
# If the event is "rest": you gain energy, the number in the second part. But your energy cannot exceed your initial energy (100). Print: "You gained {0} energy.".
# After that, print your current energy: "Current energy: {0}.".
# If the event is "order": You've earned some coins, the number in the second part. Each time you get an order, your energy decreases with 30 points.
# If you have energy to complete the order, print: "You earned {0} coins.".
# Otherwise, you should skip the order and gain 50 energy points. Print: "You had to rest!".
# In any other case you are having an ingredient, you have to buy. The second part of the event, contains the coins you have to spent and remove from your coins.
# If you are not bankrupt (coins <= 0) you've bought the ingredient successfully, and you should print ("You bought {ingredient}.")
# If you went bankrupt, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events through the day, print on the next three lines:
# "Day completed!", "Coins: {coins}", "Energy: {energy}".
# Input / Constraints
# You will receive a string, representing the working day events, separated with '|' (vertical bar): " event1|event2|event3…".
# Each event contains event name or ingredient and a number, separated by dash("{event/ingredient}-{number}")
# Output
# Print the corresponding messages, described above.


# INPUT:
# rest-2|order-10|eggs-100|rest-10

# EXPECTED OUTPUT:
# You gained 0 energy.
# Current energy: 100.
# You earned 10 coins.
# You bought eggs.
# You gained 10 energy.
# Current energy: 80.
# Day completed!
# Coins: 10
# Energy: 80


# INPUT:
# order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000

# EXPECTED OUTPUT:
# You earned 10 coins.
# You earned 10 coins.
# You earned 10 coins.
# You bought flour.
# You had to rest!
# Closed! Cannot afford oven.


energy = 100
coins = 100

working_day_events_half_separeted = input().split("|")
working_day_events = []
for el in working_day_events_half_separeted:
    string = str(el)
    working_day_events.append(string.split("-"))

completed = True
for day in working_day_events:
    if day[0] == "rest":
        if energy == 100:
            print(f"You gained {0} energy.")
        elif energy + int(day[1]) > 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        else:
            energy += int(day[1])
            print(f"You gained {int(day[1])} energy.")
        print(f"Current energy: {energy}.")
    elif day[0] == "order":
        if energy >= 30:
            energy -= 30
            coins += int(day[1])
            print(f"You earned {int(day[1])} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - int(day[1]) > 0:
            coins -= int(day[1])
            print(f"You bought {day[0]}.")
        else:
            completed = False
            print(f"Closed! Cannot afford {day[0]}.")
            break
if completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
