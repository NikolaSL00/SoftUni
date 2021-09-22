# You are driving a truck on a circle road with N petrol pumps on it.
# The petrol pumps are numbered 0 to (N−1) (both inclusive).
# For each petrol pump you will receive two pieces of information (separated by a single space):
# the amount of petrol that petrol pump will give
# the distance from that petrol pump to the next petrol pump (kilometers)
# Initially, you have a tank of infinite capacity carrying no petrol.
# The truck can start the tour at any of the petrol pumps and it will move one kilometer for each liter of
# the petrol. Calculate the first point from where the truck will be able to complete the circle.
# Consider that the truck will stop at each of the petrol pumps.

# Input
# On the first line you will receive the number of petrol pumps - N
# On the next N-lines you will receive the amount of petrol that petrol pump will give
# and the distance between that petrol pump and the next petrol pump, separated by single space

# Output
# An integer which will be the smallest index of a petrol pump from which you can start the tour

# Constraints
# 1 ≤ N ≤ 1000001
# 1 ≤ Amount of petrol, Distance ≤ 1000000000
# You will always have at least one point from where the truck will be able to complete the circle

# INPUT:
# 3
# 1 5
# 10 3
# 3 4

# OUTPUT:
# 1

# INPUT:
# 5
# 22 5
# 14 10
# 52 7
# 21 12
# 36 9

# OUTPUT:
# 0

from collections import deque

number_of_petrol_pumps = int(input())

list_of_pumps_information = []
queue = deque()

for _ in range(number_of_petrol_pumps):
    list_of_pumps_information = [int(el) for el in input().split()]
    queue.append(list_of_pumps_information)

for indx in range(number_of_petrol_pumps):
    car_fuel = 0
    completed = True

    for petrol, distance_to_next_pump in queue:
        car_fuel += petrol
        if distance_to_next_pump > car_fuel:
            completed = False
            break
        car_fuel -= distance_to_next_pump
    if completed:
        print(indx)
        break

    queue.append(queue.popleft())
