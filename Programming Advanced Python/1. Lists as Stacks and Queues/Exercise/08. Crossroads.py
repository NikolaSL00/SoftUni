# The super-spy action hero Sam has finally found some time to go on a holiday.
# He is taking his wife somewhere nice and they're going to have a really good time, but first,
# they have to get there. Even on his holiday trip,
# Sam is still going to run into some problems and the first one is getting to the airport.
# Right now, he is stuck in a traffic jam at a crossroads where a lot of accidents happen.
# Your job is to keep track of the traffic at the crossroads and report whether a crash happened or
# everyone passed the crossroads safely.
# Sam is on a single lane of cars which queue up until the light goes green.
# When it does, they start passing one by one on a flashing green light and during the free window
# before the intersecting road's light goes green. For each second only one part of a car
# (a single character) passes the crossroad. If a car is still in the middle of the crossroads when
# the free window ends, it will get hit at the first character that is still in the crossroads.

# Input
# On the first line, you will receive the duration of the green light in seconds – an integer [1 … 100]
# On the second line, you will receive the duration of the free window in seconds – an integer [0 … 100]
# On the following lines, until you receive the "END" command, you will receive one of two things:
# A car – a string containing the model of the car, or
# The command "green" which indicates the start of a green light cycle
# A green light cycle goes as follows:
# During the green light cars will enter and exit the crossroads one by one
# During the free window cars will only exit the crossroads

# Output
# If a crash happens, end the program and print:
# "A crash happened!"
# "{car} was hit at {character_hit}."
# If everything goes smoothly and you receive an "END" command, print:
# "Everyone is safe."
# "{total_cars_passed} total cars passed the crossroads."

# Constraints
# The input will be within the constaints specified above and will always be valid.
# There is no need to check it explicitly.

# Input
# On the first line, you will receive the names of the robots and their processing times in the format
# "robotName-processTime;robotName-processTime;robotName-processTime..."
# On the second line, you will get the starting time in format "hh:mm:ss"
# Next, until the "End" command, you will get a product on each line.

# Output
# Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"


# INPUT:
# 10
# 5
# Mercedes
# green
# Mercedes
# BMW
# Skoda
# green
# END

# OUTPUT:
# Everyone is safe.
# 3 total cars passed the crossroads.

# INPUT:
# 9
# 3
# Mercedes
# Hummer
# green
# Hummer
# Mercedes
# green
# END

# OUTPUT:
# A crash happened!
# Hummer was hit at e.
from collections import deque

duration_of_green_light_in_seconds = int(input())
duration_of_free_window_in_seconds = int(input())

cars_queue = deque()
passed_cars = 0
crashed_flag = False

while True:
    command = input()

    if command == "END":
        break
    elif command == "green":
        green_duration = duration_of_green_light_in_seconds
        free_window_duration = duration_of_free_window_in_seconds

        while green_duration > 0:

            if cars_queue:
                current_car = cars_queue.pop()

                if len(current_car) <= green_duration:
                    green_duration -= len(current_car)
                    passed_cars += 1
                else:
                    green_duration -= len(current_car)
                    free_window_duration += green_duration

                    if free_window_duration < 0:
                        print("A crash happened!")
                        print(f"{current_car} was hit at {current_car[free_window_duration]}.")
                        crashed_flag = True
                        break
                    else:
                        passed_cars += 1
            else:
                break
    else:
        cars_queue.appendleft(command)

    if crashed_flag:
        break

if not crashed_flag:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
