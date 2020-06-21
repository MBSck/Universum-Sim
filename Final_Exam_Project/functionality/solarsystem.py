import planets
import tools


class SolarSystem:
    """This creates the space in which the objects interact with each other"""
    def __init__(self):
        """Initializes the intrastellar objects and their changing attributes"""
        self.planets_list = []
        self.acceleration_list = []
        self.position_list = []
        self.velocity_list = []

    def add_planet(self, *args):
        """Adds planets or objects to the solarsystem"""
        # Max size of system is 20 planets
        if len(self.planets_list) < 20:
            for i in args:
                self.planets_list.append(i)

    def remove_planet(self):
        """Removes planet from the solarsystem"""
        ...

    def planetary_interaction(self):
        """Calculates the new accelerations of each of the planets"""
        self.acceleration_list = []

        for i in self.planets_list:
            a_x, a_y = i.a[0]. i.a[1]
            for j in self.planets_list:
                if i != j:
                    a_x += j.alien_acceleration(i)[0]
                    a_y += j.alien_acceleration(i)[1]

            self.acceleration_list.append([a_x, a_y])

        return self.acceleration_list

    def planetary_positions(self, start_time):
        """Utilizes Verlet integration to get the next positions of all planets for a certain timestep period"""

        for i, o in enumerate(self.planets_list):
            self.position_list.append([tools.verlet_algorithm()[0], tools.verlet_algorithm()[0]])
            self.velocity_list.append([tools.verlet_algorithm()[1], tools.verlet_algorithm()[1]])



if __name__ == "__main__":
    earth = planets.Planet("Earth", 1000000000, 3000, 10, 15)
    satellite = planets.Planet("Satellite", 100, 12, 30, 35)
    ss = SolarSystem()
    ss.add_planet(earth, satellite)
    print(ss.planetary_interaction())

    print(ss.planets_list)

