import planets
import tools


__name__ = "__solarsystem__"

class SolarSystem:
    """This creates the space in which the objects interact with each other"""
    def __init__(self):
        """Initializes the intrastellar objects"""
        self.planets = []

    def add_planet(self, *args):
        """Adds planets or objects to the solarsystem"""
        # Max size of system is 20 planets
        if len(self.planets) < 20:
            for i in args:
                self.planets.append(i)

    def planetary_interaction(self):
        """Calculates the new accelerations of each of the planets"""
        for i in self.planets:
            i.a = 0
            for j in self.planets:
                if i == j:
                    pass
                else:
                    i.a += j.alien_acceleration(i)

    def planetary_positions(self):
        """Gives the positions of all planets for a certain timespan"""


if __name__ == "__solarsystem__":
    earth = planets.Planet("Earth", 1000000000, 3000, 10, 15)
    satellite = planets.Planet("Satellite", 100, 12, 30, 35)
    ss = SolarSystem()
    ss.add_planet(earth, satellite)

    print(ss.planets)

