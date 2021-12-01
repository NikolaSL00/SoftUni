# Create a function called start_playing which will receive an instance and will return its play() method.

# Test Code:
# class Guitar:
#     def play(self):
#         return "Playing the guitar"
#
# guitar = Guitar()
# print(start_playing(guitar))

# Desired Output:
# Playing the guitar

# Test Code:
# class Children:
#     def play(self):
#         return "Children are playing"
#
# children = Children()
# print(start_playing(children))

# Desired Output:
# Children are playing


def start_playing(instance):
    return instance.play()
