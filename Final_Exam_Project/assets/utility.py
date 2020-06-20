import os
import pygame as pg

# Center the application
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Set screen
SCREEN = pg.display.set_mode((0, 0), pg.FULLSCREEN)

# Get screen size
info = pg.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h

# Set fps and clock
FPS, clock = 25, pg.time.Clock()

# Define colors
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)

# Font
font = "assets/Gameplay.ttf"

# Size of the circles/planets
BLOCK_SIZE = 50
CIRCLE_RADIUS = int(BLOCK_SIZE/2)


def text_format(message, textFont, textSize, textColor):
    """Gets a message and renders its size, text, font and color"""
    newFont = pg.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


def mouse_collison(objects, radius):
    """Gets the position of the mouse and checks if it collides with any objects in the game"""
    pos_x, pos_y = pg.mouse.get_pos()
    selected, selected_offset_x, selected_offset_y = None, 0, 0
    # Checks if the mouse collides with element
    for i, o in enumerate(objects):
        # Pythagoras a^2 + b^2 = c^2
        dx = o.centerx - pos_x
        dy = o.centery - pos_y
        distance_square = dx ** 2 + dy ** 2

        # Checks the distance between the cursor and the circle
        if distance_square <= radius[i] ** 2:
            selected = i
            selected_offset_x = o.x - pos_x
            selected_offset_y = o.y - pos_y

    return selected, selected_offset_x, selected_offset_y
