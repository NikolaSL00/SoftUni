class Player:

    def __init__(self, name: str, sprint: str, dribble: int, passing: int, shooting: int):
        self.name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError('Name can not be empty string')
        self.__name = value

    def __str__(self):
        result_string = f'Player: {self.name}\n'
        result_string += f'Sprint: {self.__sprint}\n'
        result_string += f'Dribble: {self.__dribble}\n'
        result_string += f'Passing: {self.__passing}\n'
        result_string += f'Shooting: {self.__shooting}\n'
        return result_string
