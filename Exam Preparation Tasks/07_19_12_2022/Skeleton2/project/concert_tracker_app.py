from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List = [Band]
        self.musicians: List = [Musician]
        self.concerts: List = [Concert]

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES.keys():
            raise ValueError("Invalid musician type!")

        try:
            next(filter(lambda m: m.name == name, self.musicians))
            raise Exception(f"{name} is already a musician!")
        except StopIteration:
            self.musicians.append(self.VALID_MUSICIAN_TYPES[musician_type](name, age))
            return f"{name} is now a {musician_type}."

    def create_band(self, name: str):

        try:
            next(filter(lambda b: b.name == name, self.bands))
            raise Exception(f"{name} band is already created!")
        except StopIteration:
            self.bands.append(Band(name))
            return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):

        try:
            next(filter(lambda c: c.place == place, self.concerts))
            raise Exception(f"{place} is already registered for {genre} concert!")
        except StopIteration:
            self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next(filter(lambda m: m.name == musician_name, self.musicians), None)
        band = next(filter(lambda b: b.name == band_name, self.bands), None)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.musicians.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):

        band = next(filter(lambda b: b.name == band_name, self.bands), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = next(filter(lambda m: m.name == musician_name, band.members), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands))
        self._check_member_types_in_band(band)

        concert = next(filter(lambda c: c.place == concert_place, self.concerts))
        if not self._check_if_band_can_play(band, concert):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit}$ from the {concert.genre} concert in {concert_place}."

    def _check_if_band_can_play(self, band_obj, concert_obj):
        if concert_obj.genre == "Rock":
            needed_skills = {"Singer": "sing high pitch notes",
                             "Drummer": "play the drums with drumsticks",
                             "Guitarist": "play rock"}
            for member in band_obj.members:
                if needed_skills[member.TYPE_] not in member.skills:
                    return False

        elif concert_obj.genre == "Metal":
            needed_skills = {"Singer": "sing low pitch notes",
                             "Drummer": "play the drums with drumsticks",
                             "Guitarist": "play metal"}
            for member in band_obj.members:
                if needed_skills[member.TYPE_] not in member.skills:
                    return False

        elif concert_obj.genre == "Jazz":
            needed_skills = {"Singer": "sing high pitch notes and sing low pitch notes",
                             "Drummer": "play the drums with drum brushes",
                             "Guitarist": "play jazz"}
            for member in band_obj.members:
                if needed_skills[member.TYPE_] not in member.skills:
                    return False
        return True

    def _check_member_types_in_band(self, band: Band):
        types = ["Guitarist", "Drummer", "Singer"]

        for member in band.members:
            if member.TYPE in types:
                types.pop(member.TYPE)

        if not len(types) == 0:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")
