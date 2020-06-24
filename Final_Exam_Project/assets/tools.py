from Final_Exam_Project.assets.variables import *
import pygame as pg
import abc, sys

# Make class that creates empty rectangle for menu option
# Create menu to change planet names and so on

# Useful tools for calculation and display

# ----- Classes ------


class Singleton(type):
    """Creates a singleton ~ Global Class"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SceneBase(abc.ABC):
    """Base class for the different scenes used in the games gui"""
    def __init__(self):
        """Sets the actual scene as the class inheriting this"""
        self.next = self

    @abc.abstractmethod
    def process_input(self, events, pressed_keys):
        """Takes the user input and acts on it"""
        pass

    @abc.abstractmethod
    def update(self):
        """Update method for events - takes game logic"""
        pass

    @abc.abstractmethod
    def render(self, screen):
        """Renders the screen depending on events and or user input"""
        pass

    def switch_to_scene(self, next_scene):
        """Switches to the next scene"""
        self.next = next_scene

    def terminate(self):
        """Terminates the game"""
        pg.quit()
        sys.exit()


class SelectionMenu:
    """Implements selection menu to change the values of the planets"""
    def __init__(self):
        self.start_pos = (150, 950)
        self.stop_pos = (150, 950)
        self.reset_pos = (1550, 950)

        self.start_stop_button = pg.Rect(self.start_pos[0], self.start_pos[1], 200, 50)
        self.reset_button = pg.Rect(self.reset_pos[0], self.reset_pos[1], 200, 50)

    def draw_button(self, screen, button_rect, color, text, pos_y, offset_x=0, offset_y=1.5):
        """Draw button with text on it that is in black"""
        pg.draw.rect(screen, color, button_rect)
        button_text = text_format(text, text_size=45, text_color=BLACK)
        button_rect = button_text.get_rect()
        screen.blit(button_text, (button_rect[2] + offset_x, pos_y - offset_y))


# ----- Methods ------


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
    # Maybe use scipy.integrate to solve newton DGLs

    # Calcuate verlet for every point and add it to list
    # Only then update it

    position = position - velocity * dt + (acceleration * (dt**2) * 0.5)
    velocity = velocity + acceleration * dt

    return position, velocity


if __name__ == "__main__":
    pass


