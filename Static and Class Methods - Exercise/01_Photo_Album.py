from math import ceil
from typing import List


class PhotoAlbum:

    PHOTOS_PER_PAGE = 4
    DASHES = 11
    SYMBOL = "-"

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < self.PHOTOS_PER_PAGE:
                slot = len(self.photos[page]) + 1
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {slot}"

        return "No more free slots"

    def display(self):
        result = [self.SYMBOL * self.DASHES]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(self.DASHES * self.SYMBOL)

        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
