from project.animals.animal import Mammal

class Mouse(Mammal):
    food_types = ['Vegetable', 'Fruit']
    weight_gain = 0.10

    def __init__(self, name: str, weight: float, living_region: float):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return f"Squeak"


class Dog(Mammal):
    food_types = ['Meat']
    weight_gain = 0.40

    def __init__(self, name: str, weight: float, living_region: float):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return f"Woof!"


class Cat(Mammal):
    food_types = ['Vegetable', 'Meat']
    weight_gain = 0.30

    def __init__(self, name: str, weight: float, living_region: float):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return f"Meow"


class Tiger(Mammal):
    food_types = ['Meat']
    weight_gain = 1.00

    def __init__(self, name: str, weight: float, living_region: float):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return f"ROAR!!!"
