import functionality.planets as planets
import assets.tools as tools
from assets.variables import *

# Also add logger to code and display errors correctly
# Make one pixel correspond to 1/10 au so that acceleration works more realistic


class SolarSystem(metaclass=tools.Singleton):
    """This creates the space in which the objects interact with each other.
    Singleton so it can be used in different functions and keeps all functionality"""
    def __init__(self):
        """Initializes the intrastellar objects and their changing attributes"""
        self.planets_list = []
        self.max_objects = 10
        self.system_time = 0

        # To display error messages
        self.error = False

    def add_planet(self, *args):
        """Adds planets or objects to the solar system"""
        if self.number_of_intrastellar_objects() < self.max_objects:
            for i in args:
                self.planets_list.append(i)
        else:
            # Display some error message
            self.error = True

    def remove_planet(self, planet):
        """Removes planet from the solar system"""
        self.planets_list.remove(planet)

    def get_planet(self, planet):
        """Gets specific planet from planet list"""
        if planet in self.planets_list:
            return planet

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
                    a_x += i.alien_acceleration(j)[0]
                    a_y += i.alien_acceleration(j)[1]

            acceleration_list.append([a_x, a_y])

        return acceleration_list

    def planetary_positions(self):
        """Utilizes Verlet integration to get the next positions of all planets for a certain time step period"""
        temp_pos_list, temp_vel_list = [], []
        for i, o in enumerate(self.planets_list):
            # Calculates the position and velocity for each step and saves it to the planet
            temp_pos_x, temp_v_x = tools.verlet_algorithm(o.pos_x_real, o.v_x, self.planetary_interaction()[i][0])
            temp_pos_y, temp_v_y = tools.verlet_algorithm(o.pos_y_real, o.v_y, self.planetary_interaction()[i][1])

            # Saves it to a temporary list as to not corrupt positional data for each step
            temp_pos_list.append([temp_pos_x, temp_pos_y])
            temp_vel_list.append([temp_v_x, temp_v_y])

        return temp_pos_list, temp_vel_list

    def update(self):
        """"Updates the calculated data and stores it inside the planets itself"""
        for i, o in enumerate(self.planets_list):
            o.pos_x_real, o.pos_y_real = self.planetary_positions()[0][i]
            o.v_x, o.v_y = self.planetary_positions()[1][i]

            # o.trace.append(o.rect.center)

    def reset(self):
        """This resets the class back to its empty state"""
        self.planets_list = []
        self.system_time = 0


if __name__ == "__main__":
    earth = planets.Planet(1e20, 5, 0)
    satellite = planets.Planet(1e20, 10, 0)
    moon = planets.Planet(1e20, 15, 0)
    ss = SolarSystem()
    ss.add_planet(earth, satellite, moon)
    print(ss.planetary_interaction())

    print(ss.planets_list)
    for i in ss.planets_list:
        print(i.pos_x, i.pos_y)

    for i in ss.planets_list:
        print(i.pos_x, i.pos_y)
