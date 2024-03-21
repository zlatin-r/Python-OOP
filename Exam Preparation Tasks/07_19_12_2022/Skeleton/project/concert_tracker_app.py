from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        if self._find_musician_by_name(name, self.musicians):
            raise ValueError(f"{name} is already a musician!")
        new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self._find_band_by_name(name, self.bands):
            raise ValueError(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = next(filter(lambda c: c.place == place, self.concerts), None)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{new_concert.genre} concert in {new_concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._find_musician_by_name(musician_name, self.musicians)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        band = self._find_band_by_name(band_name, self.bands)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        # TODO -> MAYBE REMOVE MUSICIAN FROM MUSICIANS...???
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._find_band_by_name(band_name, self.bands)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        musician = self._find_musician_by_name(musician_name, band.musicians)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.musicians.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self._find_band_by_name(band_name, self.bands)
        if not self._check_band_members(band):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        concert = self._find_concert_by_place(concert_place)
        if not self._check_if_band_can_play(band, concert):
            return f"The {band_name} band is not ready to play at the concert!"
        profit = self._calculate_profit(concert)
        return f"{band_name} gained {profit}$ from the {concert.genre} concert in {concert_place}."

    # helping methods:

    def _find_musician_by_name(self, name: str, collection: list):
        musician = next(filter(lambda m: m.name == name, collection), None)
        return musician

    def _find_band_by_name(self, name, collection: list):
        band = next(filter(lambda b: b.name == name, collection), None)
        return band

    def _find_concert_by_place(self, concert_place: str):
        concert = next(filter(lambda c: c.place == concert_place, self.concerts), None)
        return concert

    def _check_band_members(self, band_obj):
        types = ["Singer", "Drummer", "Guitarist"]
        members_types = [m.TYPE_ for m in band_obj.members if m.TYPE_ in types]
        return set(members_types) == set(types)

    def _check_if_band_can_play(self, band_obj, concert_obj):
        if concert_obj.genre == "Rock":
            needed_skills = {"Singer": "sing high pitch notes",
                             "Drummer": "play the drums with drumsticks",
                             "Guitarist": "play rock"}
            for member in band_obj.members:
                if not needed_skills[member.TYPE_] in member.skills:
                    return False

        elif concert_obj.genre == "Metal":
            needed_skills = {Singer: "sing low pitch notes",
                             Drummer: "play the drums with drumsticks",
                             Guitarist: "play metal"}
            for member in band_obj.members:
                if not needed_skills[member] in member.skills:
                    return False

        elif concert_obj.genre == "Jazz":
            needed_skills = {Singer: "sing high pitch notes and sing low pitch notes",
                             Drummer: "play the drums with drum brushes",
                             Guitarist: "play jazz"}
            for member in band_obj.members:
                if not needed_skills[member] in member.skills:
                    return False
        return True

    def _calculate_profit(self, concert_obj):
        profit = (concert_obj.audience * concert_obj.ticket_price) - concert_obj.expenses
        return f"{profit:.2f}"
