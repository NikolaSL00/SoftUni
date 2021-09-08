# Create a class Weapon. The __init__ method should receive the number of bullets (integer).
# Create an attribute called bullets to store them. The class should also have the following methods:
# shoot() - if there are bullets in the weapon, reduce them by 1 and return a message "shooting...".
# If there are no bullets left, return: "no bullets left".
# __repr__() - returns "Remaining bullets: {amount_of_bullets}".


class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)

# EXPECTED OUTPUT:
# shootin...
# shooting...
# shooting...
# shooting...
# shooting...
# no bullets left
# Remaining bullets: 0
