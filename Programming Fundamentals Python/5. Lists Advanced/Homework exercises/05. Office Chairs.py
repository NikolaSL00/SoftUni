# You are a facility manager at a large business center and one of your responsibilities
# is to check if each conference room in the center have enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the next n lines for each room, you will receive information about the chairs in the room and the number
# of visitors. Each chair will be presented with the char "X". Next, there will be a single space and at the end,
# the number of visitors. For example: "XXXXX 4" (5 chairs and 4 visitors).

# Keep track of the free chairs:
# If there are not enough chairs in a certain room, print the following message:
# "{needed_chairs_in_room} more chairs needed in room {number_of_room}".
# Otherwise, print: "Game On, {total_free_chairs} free chairs left"


# INPUT:
# 4
# XXXX 4
# XX 1
# XXXXXX 3
# XXX 3

# EXPECTED OUTPUT:
# Game On, 4 free chairs left


# INPUT:
# 3
# XXXXXXX 5
# XXXX 5
# XXXXXX 8

# EXPECTED OUTPUT:
# 1 more chairs needed in room 2
# 2 more chairs needed in room 3


rooms = int(input())
room_info = []
is_necessary_chairs = False
free_spaces = 0
for room in range(rooms):
    room_info.append(input().split(" "))

for index in range(len(room_info)):
    el = room_info[index]
    free_spaces += len(el[0]) - int(el[1])
    if len(el[0]) < int(el[1]):
        print(f"{abs(len(el[0]) - int(el[1]))} more chairs needed in room {index + 1}")
        is_necessary_chairs = True

if not is_necessary_chairs:
    print(f"Game On, {free_spaces} free chairs left")
