from typing import List
from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: List[str] = []

    def assign_player(self, player: Player):
        pass

