from typing import Tuple
from project.song import Song


class Album:

    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.songs = [*songs]
        self.published: bool = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {self.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published"
        if song in self.songs:
            return "Song is already in the album."

    def remove_song(self, song_name: str):
        if song_name in self.songs:
            self.songs.remove(song_name)
            return f"Removed song {song_name} from album {self.name}."
        if song_name not in self.songs:
            return "Song is not in the album."
        if self.published:
            return f"Cannot remove songs. Album is published."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):
        songs_details = "\n".join(f"== {s.get_info()}" for s in self.songs)
        return f"Album {self.name}\n{songs_details}"

