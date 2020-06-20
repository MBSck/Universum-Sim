class Planet:
    """This checks the values and the behaviour of the planet"""
    def __init__(self, mass, radius, velocity):
        """Initializes the planets values"""
        ...

    @property
    def acceleration(self):
        """Calculates the acceleration"""
        ...

    @acceleration.setter
    def acceleration(self):
        """Sets the velocity of the planet"""
        ...

help(property)