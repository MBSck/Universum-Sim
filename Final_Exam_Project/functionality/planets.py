from Final_Exam_Project.assets.variables import *


class Planet:
    """This checks the values and the behaviour of the planet"""
    def __init__(self, name: str, mass: float, pos_x: int, pos_y: int,
                 rect_size_x: int = BLOCK_SIZE, rect_size_y: int = BLOCK_SIZE,
                 radius: int = CIRCLE_RADIUS, v_x: int = 0, v_y: int = 0):
        """Initializes the planets values"""
        self.name = name
        self.mass = mass
        self.radius = radius
        self.v_x, self.v_y = v_x, v_y
        self.pos_x_real, self.pos_y_real = pos_x*PIXEL_REAL, pos_y*PIXEL_REAL
        self.rect_size_x, self.rect_size_y = rect_size_x, rect_size_y

    def __repr__(self):
        """Shows the class name if outputted"""
        return self.name

    def pos_x(self):
        """Gets the pixel position after the physical has been calculated"""
        return self.pos_x_real/PIXEL_REAL

    def pos_y(self):
        """Gets the pixel position after the physical has been calculated"""
        return self.pos_y_real/PIXEL_REAL

    @property
    def rect(self):
        """Gets the rect object"""
        return pg.Rect(self.pos_x(), self.pos_y(), self.rect_size_x, self.rect_size_y)

    def alien_acceleration(self, other):
        """The acceleration this body enacts on another"""
        distance_squared = math.sqrt((self.pos_x_real - other.pos_x_real) ** 2
                                     + (self.pos_y_real - other.pos_y_real) ** 2)
        nominator_x, nominator_y = self.mass * (self.pos_x_real - other.pos_x_real), \
                                   self.mass * (self.pos_y_real - other.pos_y_real)

        return gravitational_constant * nominator_x / (distance_squared ** 3), \
            gravitational_constant * nominator_y / (distance_squared ** 3)


if __name__ == "__main__":
    earth = Planet("Earth", 1e09, 3000, 10, 15)
    satellite = Planet("Satellite", 100, 12, 30, 35)
    print(math.sqrt(20**2+20**2))
    print(gravitational_constant*100/(28.284271247461902**2))
