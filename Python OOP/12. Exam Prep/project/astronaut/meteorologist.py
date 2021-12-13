from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    breath_value = 15

    def __init__(self, name):
        super().__init__(name, 90)
