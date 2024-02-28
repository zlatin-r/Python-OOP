from typing import Tuple
from project.song import Song


class Album:

    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.songs = [*songs]
        self.published: bool = False

    def add_song(self, song: Song):

