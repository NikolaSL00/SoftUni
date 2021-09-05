# Create a function which calculates and returns the area of a rectangle by given width and height.
# Print the result on the console.

# INPUT:
# 3
# 4

# EXPECTED OUTPUT:
# 12


# INPUT:
# 6
# 2

# EXPECTED OUTPUT:
# 12


def rect_area(w, h):
    return w * h


width = int(input())
height = int(input())

print(rect_area(width, height))
