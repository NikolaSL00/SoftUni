# Somewhere in the future, there is a robotics factory. The current project is assembly line robots.
# Each robot has a processing time – it is the time in seconds the robot needs to process a product.
# When a robot is free it should take a product for processing and log his name, product and processing start time.
# Each robot processes a product coming from the assembly line.
# A product is coming from the line each second (so the first product should appear at [start time + 1 second]).
# If a product passes the line and there is not a free robot to take it,
# it should be queued at the end of the line again.
# The robots are standing on the line in the order of their appearance.

# Input
# On the first line, you will receive the names of the robots and their processing times in the format
# "robotName-processTime;robotName-processTime;robotName-processTime..."
# On the second line, you will get the starting time in format "hh:mm:ss"
# Next, until the "End" command, you will get a product on each line.

# Output
# Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"


# INPUT:
# ROB-15;SS2-10;NX8000-3
# 8:00:00
# detail
# glass
# wood
# apple
# End

# OUTPUT:
# ROB - detail [08:00:01]
# SS2 - glass [08:00:02]
# NX8000 - wood [08:00:03]
# NX8000 - apple [08:00:06]

# INPUT:
# ROB-8
# 7:59:59
# detail
# glass
# wood
# sock
# End

# OUTPUT:
# ROB - detail [08:00:00]
# ROB - wood [08:00:08]
# ROB - glass [08:00:16]
# ROB - sock [08:00:24]


from collections import deque
from math import floor


class Robot:
    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time
        self.busy_until = 0


def get_seconds_from_time(time: str):
    hours, minutes, seconds = [int(x) for x in time.split(":")]
    return hours * 60 * 60 + minutes * 60 + seconds


def get_time_from_seconds(seconds: int):
    hours = seconds // 3600
    minutes = floor((seconds / 60) % 60)
    seconds = seconds % 60
    hours %= 24
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots = []
robots_input = input().split(";")

for robot_input in robots_input:
    robot_name, robot_processing_time = robot_input.split("-")
    robots.append(Robot(robot_name, int(robot_processing_time)))

start_time_in_seconds = get_seconds_from_time(input())

queue_with_products = deque()

while True:
    item = input()
    if item != "End":
        queue_with_products.append(item)
    else:
        break

while queue_with_products:
    current_item = queue_with_products[0]
    start_time_in_seconds += 1
    found_robot = False

    for robot in robots:
        if start_time_in_seconds >= robot.busy_until:
            robot.busy_until = start_time_in_seconds + robot.processing_time
            found_robot = True
            print(f"{robot.name} - {current_item} [{get_time_from_seconds(start_time_in_seconds)}]")
            break
    if found_robot:
        queue_with_products.popleft()
    else:
        queue_with_products.append(queue_with_products.popleft())
