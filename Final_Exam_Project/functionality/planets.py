import math
import pygame as pg
from variables import *

# The gravitational constant in m**3 kg**-1 s**-2
gravitational_constant = 6.67408e-11

# make iterators for planets so values can be called
# optimize with the g in front
# Light speed optimization final communication speed

# make rect and rect size properties


class Planet:
    """This checks the values and the behaviour of the planet"""
    def __init__(self, name: str, mass: int, pos_x: int, pos_y: int,
                 rect_size_x: int = BLOCK_SIZE, rect_size_y: int = BLOCK_SIZE,
                 radius: int = CIRCLE_RADIUS, v_x: int = 0, v_y: int = 0):
        """Initializes the planets values"""
        self.name = name
        self.mass = mass
        self.radius = radius
        self.v_x, self.v_y = v_x, v_y
        self.pos_x, self.pos_y = pos_x, pos_y
        self.rect_size_x, self.rect_size_y = rect_size_x, rect_size_y

    def __repr__(self):
        return self.name

    @property
    def rect(self):
        """Gets the rect object"""
        return pg.Rect(self.pos_x, self.pos_y, self.rect_size_x, self.rect_size_y)

    def distance_to_other(self, other):
        """Calculates the euclidic distance of the pixels, split into x and y values"""
        distance_squared = math.sqrt((self.pos_x - other.pos_x)**2 + (self.pos_y - other.pos_y)**2)
        return (self.pos_x - other.pos_x)/(distance_squared**3),\
               (self.pos_y - other.pos_y)/(distance_squared**3)

    def alien_acceleration(self, other):
        """The acceleration this body enacts on another"""
        return gravitational_constant * (self.mass / ((self.distance_to_other(other)[0]) ** 2)),\
            gravitational_constant * (self.mass / ((self.distance_to_other(other)[1]) ** 2))


if __name__ == "__main__":
    earth = Planet("Earth", 1000000000, 3000, 10, 15)
    satellite = Planet("Satellite", 100, 12, 30, 35)
    print(math.sqrt(20**2+20**2))
    print(gravitational_constant*100/(28.284271247461902**2))
