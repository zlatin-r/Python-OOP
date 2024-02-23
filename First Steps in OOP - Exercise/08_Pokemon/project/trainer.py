from typing import List
from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon):
        pass

    def release_pokemon(self, pokemon_name: str):
        pass

    def trainer_data(self):
        pass
