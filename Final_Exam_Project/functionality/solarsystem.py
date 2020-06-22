import planets
import tools

# For testing
import matplotlib.pyplot as plt


# Make solar system into Singleton
# Also add logger to code
# make rect size and radius into properties

class SolarSystem(metaclass=tools.Singleton):
    """This creates the space in which the objects interact with each other.
    Singleton so it can be used in different functions and keeps all functionality"""
    def __init__(self):
        """Initializes the intrastellar objects and their changing attributes"""
        self.planets_list = []
        self.max_objects = 20

    def add_planet(self, *args):
        """Adds planets or objects to the solarsystem"""
        if self.number_of_intrastellar_objects() < self.max_objects:
            for i in args:
                self.planets_list.append(i)
        else:
            # Display some error message
            ...

    def remove_planet(self, planet):
        """Removes planet from the solarsystem"""
        self.planets_list.remove(planet)

    def get_planet(self, planet):
        """Gets specific planet from planet list"""
        for i in self.planets_list:
            if i == planet:
                return i

    def number_of_intrastellar_objects(self):
        """Returns the number of objects in list"""
        return len(self.planets_list)

    def planetary_interaction(self):
        """Calculates the new accelerations of each of the planets"""
        acceleration_list = []
        for i in self.planets_list:
            a_x, a_y = 0, 0
            for j in self.planets_list:
                if i != j:
                    a_x += j.alien_acceleration(i)[0]
                    a_y += j.alien_acceleration(i)[1]

            acceleration_list.append([a_x, a_y])

        return acceleration_list

    def planetary_positions(self):
        """Utilizes Verlet integration to get the next positions of all planets for a certain timestep period"""

        for i, o in enumerate(self.planets_list):
            # Calculates the position and velocity for each step and saves it to the planet
            o.pos_x, o.v_x = tools.verlet_algorithm(o.pos_x, o.v_x, self.planetary_interaction()[i][0])
            o.pos_y, o.v_y = tools.verlet_algorithm(o.pos_y, o.v_y, self.planetary_interaction()[i][1])


if __name__ == "__main__":
    earth = planets.Planet("Earth", 150, 200, 10, 15, 1, 0)
    satellite = planets.Planet("Satellite", 100, 12, 30, 35, 0, 0)
    ss = SolarSystem()
    ss.add_planet(earth, satellite)
    print(ss.planetary_interaction())

    print(ss.planets_list)
    print(satellite.pos_x, satellite.pos_y)

    # Checking trajectories with matplotlib
    x_list, y_list = [], []
    for i in range(100):
        ss.planetary_positions()
        x_list.append(satellite.pos_x)
        y_list.append(satellite.pos_y)

    print(satellite.pos_x, satellite.pos_y)

    plt.plot(x_list, y_list)
    plt.savefig("../assets/planet_position.png")



