# Create a class Zoo. It should have a class attribute called __animals that stores the total count
# of the animals in the zoo. The __init__ method should only receive the name of the zoo.
# There you should also create 3 empty lists (mammals, fishes, birds).
# The class should also have 2 more methods:

# ⦁	add_animal(species, name) - based on the species adds the name to the corresponding list
# ⦁	get_info(species) - based on the species returns a string in the following format:
# "{Species} in {zoo_name}: {names}

# Total animals: {total_animals}"

# On the first line you will receive the name of the zoo. On the second line you will receive number n.
# On the next n lines, you will receive animal info in the format: "{species} {name}".
# Add the animal to the zoo to the corresponding list. The "species" command will be mammal, fish, or bird.
# On the final line you will receive a species. At the end, print the info for that species and the total count
# of animals in the zoo.

# INPUT:
# Great Zoo
# 5
# mammal lion
# mammal bear
# fish salmon
# bird owl
# mammal tiger
# mammal

# EXPECTED OUTPUT:
# Mammals in Great Zoo: lion, bear, tiger
# Total animals: 5

class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_animals_count(self):
        return self.__animals

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}"


name = input()
n = int(input())

zoo = Zoo(name)

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)
searched_spec = input()
print(zoo.get_info(searched_spec))
print(f"Total animals: {zoo.get_animals_count()}")
