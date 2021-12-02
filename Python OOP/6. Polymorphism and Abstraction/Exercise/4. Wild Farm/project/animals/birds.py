from project.animals.animal import Bird

class Owl(Bird):
    food_types = ['Meat']
    weight_gain = 0.25

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return f"Hoot Hoot"


class Hen(Bird):
    food_types = ['Vegetable', 'Fruit', 'Meat', 'Seed']
    weight_gain = 0.35

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return f"Cluck"
