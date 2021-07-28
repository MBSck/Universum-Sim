from variables import *

"""Useful tools for calculation and display"""

# TODO: Make class that creates empty rectangle for menu option
# TODO: Create menu to change planet names and so on

"""-----Classes------"""


class Singleton(type):
    """Creates a singleton ~ Global Class"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SceneBase(abc.ABC):
    """Base class for the different scenes used in the games gui"""

    def __init__(self) -> None:
        """Sets the actual scene as the class inheriting this"""

        self.next = self

    @abc.abstractmethod
    def process_input(self, events, pressed_keys) -> None:
        """Takes the user input and acts on it"""

        pass

    @abc.abstractmethod
    def update(self) -> None:
        """Update method for events - takes game logic"""

        pass

    @abc.abstractmethod
    def render(self, screen) -> None:
        """Renders the screen depending on events and or user input"""

        pass

    def switch_to_scene(self, next_scene) -> None:
        """Switches to the next scene"""

        self.next = next_scene

    def terminate(self) -> None:
        """Terminates the game"""

        pg.quit()
        sys.exit()


"""-----Methods------"""


def text_format(text, text_size, text_color, text_font=font):
    """Template for creating text in pygame"""

    new_font = pg.font.Font(text_font, text_size)
    new_text = new_font.render(text, 0, text_color)

    return new_text


def mouse_collison(objects):
    """Gets the position of the mouse and checks if it collides with any objects in the game"""

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
    """This calculats the second order Taylor solution to the newton DGLs"""

    # TODO: Maybe use scipy.integrate to solve newton DGLs
    # TODO: Calcuate verlet for every point and add it to list and only then update it

    position = position - velocity * dt + (acceleration * (dt**2) * 0.5)
    velocity = velocity + acceleration * dt

    return position, velocity


def runge_kutta_method(f, t0: int, y0: int, h: int = TIMESTEP):
    """Iterative method that include the Euler-method and yields
    approximate solutions for ordinary differential equations

    Parameters
        f: The basic function for runge-kutta, has to accept two params
        t0 (int): The starting time
        y0 (int): The starting position
        h (int): The step-size of the approximation

    Returns:
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
    print(runge_kutta_method.__doc__)
