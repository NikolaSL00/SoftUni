from collections import deque

fireworks_effects = deque([int(x) for x in input().split(", ")])
explosive_power = deque([int(x) for x in input().split(", ")])

dictionary = {
    "Palm": 0,
    "Willow": 0,
    "Crossette": 0
}

successfully_prepared_flag = False

while fireworks_effects and explosive_power:
    first_effect = fireworks_effects.popleft()
    if first_effect <= 0:
        continue

    last_power = explosive_power.pop()
    while last_power <= 0 and explosive_power:
        if explosive_power:
            last_power = explosive_power.pop()
        else:
            break
    if last_power <= 0:
        fireworks_effects.appendleft(first_effect)
        continue

    sum_of_elements = last_power + first_effect
    if sum_of_elements % 15 == 0:
        dictionary["Crossette"] += 1
    elif sum_of_elements % 3 == 0:
        dictionary["Palm"] += 1
    elif sum_of_elements % 5 == 0:
        dictionary["Willow"] += 1
    else:
        first_effect -= 1
        fireworks_effects.append(first_effect)
        explosive_power.append(last_power)

    if dictionary["Palm"] >= 3 and dictionary["Willow"] >= 3 and dictionary["Crossette"] >= 3:
        successfully_prepared_flag = True
        break
if successfully_prepared_flag:
    print("Congrats! You made the perfect firework show!")
    if fireworks_effects:
        print(f"Firework Effects left: {(', ').join([str(x) for x in fireworks_effects])}")
    if explosive_power:
        print(f"Explosive Power left: {(', ').join([str(x) for x in explosive_power])}")

    print(f"Palm Fireworks: {dictionary['Palm']}")
    print(f"Willow Fireworks: {dictionary['Willow']}")
    print(f"Crossette Fireworks: {dictionary['Crossette']}")

else:
    print("Sorry. You can't make the perfect firework show.")
    if fireworks_effects:
        print(f"Firework Effects left: {(', ').join([str(x) for x in fireworks_effects])}")
    if explosive_power:
        print(f"Explosive Power left: {(', ').join([str(x) for x in explosive_power])}")

    print(f"Palm Fireworks: {dictionary['Palm']}")
    print(f"Willow Fireworks: {dictionary['Willow']}")
    print(f"Crossette Fireworks: {dictionary['Crossette']}")
