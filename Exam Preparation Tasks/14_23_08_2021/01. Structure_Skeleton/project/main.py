from project.astronaut import astronaut_repository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.space_station import SpaceStation

a3 = Biologist("Astronaut3")
a4 = Geodesist("Astronaut4")
a5 = Biologist("Astronaut5")
a6 = Meteorologist("Astronaut6")
a7 = Biologist("Astronaut7")
p1 = Planet("planet1")
p2 = Planet("planet2")
p3 = Planet("planet3")
p4 = Planet("planet4")

app = SpaceStation()
print(app.add_astronaut("Geodesist", "George"))
print(app.add_astronaut("Meteorologist", "Misho"))
print(app.add_astronaut("Biologist", "Stefan"))
print(app.add_astronaut("Meteorologist", "Ignat"))
print(app.add_astronaut("Geodesist", "Peter"))
