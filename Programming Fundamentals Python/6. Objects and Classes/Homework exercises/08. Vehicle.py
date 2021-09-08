# Create a class Vehicle. The __init__ method should receive a type (str), a model (str), and a price (int).
# You should also set an owner to None. The class should have the following methods:
# buy(money, owner)
# If the person has enough money and the vehicle has no owner, sets the owner to the given one and returns:
# "Successfully bought a {type}. Change: {change}". Change should be formatted to the second decimal place.
# If the money is not enough, return: "Sorry, not enough money"
# If the car already has an owner, return: "Car already sold"
# sell() - if the car has an owner, set it to None again. Otherwise, return: "Vehicle has no owner"
# __repr__() - returns "{model} {type} is owned by: {owner}" if the vehicle has an owner. Otherwise,
# return: "{model} {type} is on sale: {price}"


class Vehicle:
    def __init__(self, type: str, model: str, price: int):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        if self.owner == None and self.price <= money:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {(money - self.price):.2f}"
        elif self.owner == None and self.price > money:
            return "Sorry, not enough money"
        elif self.owner != None:
            return "Car already sold"

    def sell(self):
        if self.owner != None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner == None:
            return f"{self.model} {self.type} is on sale: {self.price}"
        else:
            return f"{self.model} {self.type} is owned by: {self.owner}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)

# EXPECTED OUTPUT:
# Sorry, not enough money
# Successfully bought a car. Change: 5000.00
# BMW car is owned by: George
# BMW car is on sale: 30000
