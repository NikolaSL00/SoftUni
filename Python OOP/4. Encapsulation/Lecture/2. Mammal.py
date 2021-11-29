# Create a class called Mammal. Upon initialization, it should receive a name, a type, and a sound. Create a class attribute called kingdom which should not be accessed outside the class and set it to be "animals". Create three more instance methods:
# make_sound() - returns a string in the format "{name} makes {sound}"
# get_kingdom() - returns the private kingdom attribute
# info() - returns a string in the format "{name} is of type {type}"

# Test Code:
# mammal = Mammal("Dog", "Domestic", "Bark")
# print(mammal.make_sound())
# print(mammal.get_kingdom())
# print(mammal.info())

# Desired Output:
# Dog makes Bark
# animals
# Dog is of type Domestic

class Mammal:
    __kingdom = 'animals'

    def __init__(self, name, type, sound):
        self.__set_name(name)
        self.__set_type(type)
        self.__set_sound(sound)

    def __set_name(self, new_name):
        if new_name is None:
            raise "Name can not be None"
        self.name = new_name

    def __set_type(self, new_type):
        if new_type is None:
            raise "Name can not be None"
        self.type = new_type

    def __set_sound(self, new_sound):
        if new_sound is None:
            raise "Name can not be None"
        self.sound = new_sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"

