from assets.variables import *

"""Useful tools for calculation and display"""

# TODO: Make class that creates empty rectangle for menu option
# TODO: Create menu to change planet names and so on

"""-----Classes------"""


class Singleton(type):
    """Creates a singleton ~ Global Class

    Methods
    ----------
    __call__(*args, **kwargs):
        Checks if class is instanced already, if not creates a single instance
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Checks if class is instanced already, if not creates a single instance

        Parameters
        ----------
            *args: Any
                Arguments passed
            **kwargs: Any
                Keyword arguments passed

        Returns
        -------
        Class instance
        """

        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SceneBase(abc.ABC):
    """Base class for the different scenes used in the game's gui.
    This is a base class and therefore all its methods are abstract and
    inherited by the abc-class.

    Attributes
    ----------
    next: class
        sets the next scene class

    Methods
    ----------
    process_input(events, pressed_keys):
        Gets the user input and acts on it
    update():
        Updates the screen for events - takes game logic into account
    render(screen):
        Renders the elements on the screen depending on events and/or user input
    switch_to_scene(next_scene):
        Switches to the next scene by creating an instance of the next scene class
    terminate():
        Static method, which terminates the game by calling the relevant pygame- and sys-functions
    """

    def __init__(self) -> None:
        """Sets the actual scene as the class inheriting this

        Returns
        ----------
        None
        """

        self.next = self

    @abc.abstractmethod
    def process_input(self, events, pressed_keys) -> None:
        """Gets the user input and acts on it

        Parameters
        -----------
        events:
            the game events from pygame

        pressed_keys:
            the keys pressed by the user

        Returns
        ----------
        None:
            abstract method returns nothing
        """

        pass

    @abc.abstractmethod
    def update(self) -> None:
        """Updates the screen for events - takes game logic into account

        Returns
        ----------
        None:
            abstract method returns nothing
        """

        pass

    @abc.abstractmethod
    def render(self, screen) -> None:
        """Renders the elements on the screen depending on events and/or user input

        Parameters
        -----------
        screen:
            the screen pygame displays on

        Returns
        ----------
        None:
            abstract method returns nothing
        """

        pass

    def switch_to_scene(self, next_scene) -> None:
        """Switches to the next scene by creating an instance of the next scene class


        Parameters
        -----------
        next_scene:
            the scene class that should be switched to
        """

        self.next = next_scene

    @staticmethod
    def terminate() -> None:
        """Static method, which terminates the game by calling the relevant pygame- and sys-functions"""

        pg.quit()
        sys.exit()


"""-----Methods------"""


def text_format(text: str, text_size: int, text_color: tuple, text_font_location: str = font):
    """Template for creating text in pygame. Reformation of the size and color

    Parameters:
        text (str): The input text to be formatted
        text_size (int): The text size of the formatted text
        text_color (tuple): The text color of the formatted text
        text_font_location (str): Location of the font used for the text

    Returns:
        new_text (str): The completely refomatted text
    """

    return pg.font.Font(text_font_location, text_size).render(text, 0, text_color)


def mouse_collision(objects):
    """Gets the position of the mouse and checks if it collides with any objects in the game

    Parameters:
        objects: All objects that are in the game

    Returns:
        selected: The by the cursor selected object
        selected_offset_x:
        selected_offset_y:
    """

    pos_x, pos_y = pg.mouse.get_pos()
    selected, selected_offset_x, selected_offset_y = None, 0, 0

    # Checks if the mouse collides with element
    for i in objects:

        # Pythagoras a^2 + b^2 = c^2
        dx = i.rect.centerx - pos_x
        dy = i.rect.centery - pos_y
        distance_square = dx ** 2 + dy ** 2

        # Checks the distance between the cursor and the circle
        if distance_square <= i.radius ** 2:
            selected = i

            # Maybe different approach needed instead of .rect.x
            selected_offset_x = i.rect.x - pos_x
            selected_offset_y = i.rect.y - pos_y

    return selected, selected_offset_x, selected_offset_y


def verlet_algorithm(position: int, velocity: int, acceleration: int, dt: int = TIMESTEP):
    """This calculates the second order Taylor solution to the newton DGLs

    Parameters:
        position (int): The starting position
        velocity (int): The starting velocity
        acceleration (int): The acceleration the object experiences
        dt (int): The time-step for each iteration

    Returns:
        position (int): The new position after the numerical approximation
        velocity (int): The new velocity after the numerical approximation
    """

    # TODO: Maybe use scipy.integrate to solve newton DGLs
    # TODO: Calcuate verlet for every point and add it to list and only then update it

    return position - velocity * dt + (acceleration * (dt**2) * 0.5), velocity + acceleration * dt


def runge_kutta_method(f, t0: int, y0: int, h: int = TIMESTEP):
    """Iterative method that include the Euler-method and yields
    approximate solutions for ordinary differential equations

    Parameters
        f: The basic function for runge-kutta, has to accept two params
        t0 (int): The starting time
        y0 (int): The starting position
        h (int): The step-size of the approximation

    Returns
        t1 (int): The new time
        y1 (int): The new position
    """

    # Gets the k values
    k1 = f(t0, y0)
    k2 = f(t0+h/2, y0+h*k1/2)
    k3 = f(t0+h/2, y0+h*k2/2)
    k4 = f(t0+h, y0+h*k3)

    return t0+h, y0+h/6*(k1+2*k2+2*k3+k4)


if __name__ == "__main__":
    print(SceneBase.__doc__)
