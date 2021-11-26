from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name:str):
        self.name = name
        self.pokemons = list()

    def add_pokemon(self, Pokemon):
        if not Pokemon in self.pokemons:
            self.pokemons.append(Pokemon)
            return f"Caught {Pokemon.pokemon_details()}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name:str):
        for el in self.pokemons:
            if el.name == pokemon_name:
                self.pokemons.remove(el)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = ""
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}"
        for el in self.pokemons:
            result += f"\n- {el.pokemon_details()}"
        return result

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())