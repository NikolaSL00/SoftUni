# Create a class Circle. In the __init__ method the circle should only receive one parameter - its diameter.
# Create a class attribute called __pi that is equal to 3.14. The class should also have the following methods:
# ⦁	calculate_circumference() - returns the circumference of the circle
# ⦁	calculate_area() - returns the area of the circle
# ⦁	calculate_area_of_sector(angle) - gives the central angle in degrees, returns the area that fills the sector
# Notes: Search the formulas in the internet.
# Name your methods and variables exactly as in the description! Submit only the class.
# Test your class before submitting!


class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.__pi * self.diameter

    def calculate_area(self):
        radius = self.diameter / 2
        return self.__pi * (radius ** 2)

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * self.calculate_area()


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")

# EXPECTED OUTPUT:
# 31.40
# 78.50
# 1.09
