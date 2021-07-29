from assets.variables import *

# TODO: Make planets names show under their dots
# TODO: Make radius work
# TODO: Make realistic units work


class Planet:
    """This checks the values and the behaviour of the planet

    Attributes
    ----------
    name: str
        the planet's name
    mass: float
        the planet's mass
    trace: list
        the planet's trace
    trace_size: int
        the size of the planet's trace
    v_x: int
        the planet's x-velocity
    v_y: int
        the planet'S y-velocity
    color: tuple
        the planet's color
    radius: int
        the planet's radius
    pos_x: int
        the planet's x-position
    pos_y: int
        the planet's y-position
    rect_size_x: int
        the planet's x-rect size
    rect_size_y: int
        the planet's y-rect size
    pos_x_real: int
        the planet's real x-position on the screen
    pos_y_real: int
        the planet's real y-position on the screen
    density: float
        the planet's density

    Methods
    ----------
    collision_addition(other):
        Adds two planets together, when they are colliding
    alien_acceleration(other):
        The acceleration this body enacts on another
    """

    def __init__(self, mass: float, pos_x: int, pos_y: int,
                 v_x: int = 0, v_y: int = 0, rect_size_x: int = BLOCK_SIZE,
                 rect_size_y: int = BLOCK_SIZE, radius: int = rnd.choice(range(1, 25)),
                 color: tuple = None) -> None:
        """Initializes the planets values

        Parameters
        ----------
        mass: float
            the planet's mass
        pos_x: int
            the planet's x-position
        pos_y: int
            the planet's y-position
        v_x: int
            the planet's x-velocity
        v_y: int
            the planet's y-velocity
        rect_size_x: int
            the - for pygame needed - x-rect size of the planet
        rect_size_y: int
            the - for pygame needed - y-rect size of the planet
        radius: int
            the planet's radius
        color: tuple
            the planet's color
        """

        # Make radius property that updates itself as well as trace-size and rect size
        self.name = rnd.choice(generic_name_list)
        self.mass = mass
        self.trace = []
        self.trace_size = BLOCK_SIZE/10
        self.v_x, self.v_y = v_x, v_y

        # Get random color or player selected one
        if color is not None:
            self.color = color
        else:
            self.color = rnd.choice(list(colors.values()))

        # Values used for setters and behind the scenes update, never overwrite!
        self.__radius = radius
        self.__pos_x, self.__pos_y = pos_x, pos_y
        self.__rect_size_x, self.__rect_size_y = rect_size_x, rect_size_y

        # Gets physical accurate position
        self.pos_x_real, self.pos_y_real = self.__pos_x*PIXEL_REAL, self.__pos_y*PIXEL_REAL

    @property
    def pos_x(self):
        """Gets the pixels x position after the physical value has been calculated"""

        return self.pos_x_real/PIXEL_REAL

    @pos_x.setter
    def pos_x(self, pos_x) -> None:
        """Sets the pixel x position if needed for UI"""

        self.__pos_x = pos_x

    @property
    def pos_y(self):
        """Gets the pixels y position after the physical value has been calculated"""

        return self.pos_y_real/PIXEL_REAL

    @pos_y.setter
    def pos_y(self, pos_y) -> None:
        """Sets the pixel y position if needed for UI"""

        self.__pos_y = pos_y

    @property
    def rect(self):
        """Gets the rect object"""

        return pg.Rect(self.pos_x, self.pos_y, self.rect_size_x, self.rect_size_y)

    @property
    def radius(self):
        """Gets the radius"""

        # TODO: Might be wrong as volume doesn't increase with mass linear
        # TODO: Radius should be depending on volume add that and density

        return int(self.__rect_size_x/2)

    @radius.setter
    def radius(self, radius) -> None:
        """Sets the radius"""

        self.__radius = radius

    @property
    def density(self):
        """Gets the density of object

        Not yet implemented
        """

        return

    @property
    def rect_size_x(self):
        """Getter for the x-rect size of the planet

        Returns
        ----------
            multiplies the __radius by 2 to get the x-rect size
        """

        return self.__radius*2

    @rect_size_x.setter
    def rect_size_x(self, rect_size: int) -> None:
        """Sets the planet's y-rect size

        Parameters
        ----------
        rect_size: int
            the pygame's planet's rect size

        Returns
        ----------
        None
        """

        self.__rect_size_x = rect_size

    @property
    def rect_size_y(self):
        """Gets the rect_size_y

        Returns
        ----------
        rect_size_y: int
            multiplies the __radius by 2 to get the y-rect size
        """

        return self.__radius*2

    @rect_size_y.setter
    def rect_size_y(self, rect_size: int) -> None:
        """Sets the planet's y-rect size

        Parameters
        ----------
        rect_size: int
            the pygame's planet's rect size

        Returns
        ----------
        None
        """

        self.__rect_size_y = rect_size

    '''
    def draw_trace(self, screen):
        """Draws a trace of all the planets in the solar system"""
        for i, o in enumerate(self.trace):
            pg.draw.circle(screen, self.color, o[i], self.radius)
    '''

    def collision_addition(self, other) -> None:
        """Adds two planets together, when they are colliding

        Parameters
        ----------
        other: Planet
            other planet that is interacting with this one

        Returns
        ----------
        None
        """

        # TODO: Maybe implement mass loss and explosion later on
        # TODO: Think about momentum conservation and volume and radius increase by mass increase
        # TODO: Collision is bigger than the real size of the circles! Check
        # TODO: Think about addition, doesn't add values up physically correct

        self.mass += other.mass
        self.rect_size_x += other.rect_size_x
        self.rect_size_y += other.rect_size_y
        self.v_x += other.v_x
        self.v_y += other.v_y
        self.pos_x_real = (self.pos_x_real + other.pos_x_real)/2
        self.pos_y_real = (self.pos_y_real + other.pos_y_real)/2

    def alien_acceleration(self, other):
        """The acceleration this body enacts on another

        Parameters
        ----------
        other: Planet
            other planet that is interacting with this one

        Returns
        ----------
        x-acceleration:
            the acceleration the planet experiences in the x-direction
        y-acceleration:
            the acceleration the planet experiences in the y-direction
        """

        distance_squared = np.sqrt((self.pos_x_real - other.pos_x_real) ** 2
                                   + (self.pos_y_real - other.pos_y_real) ** 2)
        nominator_x, nominator_y = self.mass * (self.pos_x_real - other.pos_x_real), \
                                   self.mass * (self.pos_y_real - other.pos_y_real)

        return gravitational_constant * nominator_x / (distance_squared ** 3), \
            gravitational_constant * nominator_y / (distance_squared ** 3)


if __name__ == "__main__":
    earth = Planet(1e09, 3000, 10, 15)
    satellite = Planet(100, 12, 30, 35)
    print(np.sqrt(20**2+20**2))
    print(gravitational_constant*100/(28.284271247461902**2))
