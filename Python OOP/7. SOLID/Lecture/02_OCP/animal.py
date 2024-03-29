class Animal:
    _sound = ''
    _species = ''

    def get_species(self):
        return self._species

    def get_sound(self):
        return self._sound


class Cat(Animal):
    _sound = 'meow'
    _species = 'cat'


class Dog(Animal):
    _sound = 'woof-woof'
    _species = 'dog'


def animal_sound(animals_list: list):
    for animal in animals_list:
        print(animal.get_sound())


animals_list = [Cat(), Dog()]
animal_sound(animals_list)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
