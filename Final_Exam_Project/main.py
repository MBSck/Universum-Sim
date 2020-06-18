import os, sys
import pygame as pg
from pygame.locals import *

"""This is a planet creating tool that leads to a functioning solar system, add some future features like
black holes and such"""

# Startbedigungen für planeten z.B. mit Pfeil in Richtung usw.

# Planeten können per Click erstellt werden

# Sollen sich gravitationstechnisch richtig verhalten

# Make main menu and editor function so that you can create new planets and destroy them and soo forth and drag them
# around

# Center the application
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Set screen
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 800
SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Set fps and clock
FPS, clock = 25, pg.time.Clock()

# Define colors
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)

# Font
font = "Gameplay.ttf"

# Get screen size
info = pg.display.Info()
sw, sh = info.current_w, info.current_h

# Fill the background of the screen
SCREEN.fill(BLACK)

# Size of the circles/planets
BLOCK_SIZE = 50
CIRCLE_RADIUS = int(BLOCK_SIZE/2)


def text_format(message, textFont, textSize, textColor):
    """Gets a message and renders its size, text, font and color"""
    newFont = pg.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


def main_menu():
    """This is the intro of our program, starting menu"""
    menu = True
    selected = "start"
    counter = 0

    while menu:
        for event in pg.event.get():
            # Checks if the user presses the 'X' or closes the window
            if event.type == QUIT:
                menu = False

            # Checks for keypress
            if event.type == KEYDOWN:

                # Closes the window if 'esc' is pressed
                if event.key == pg.K_ESCAPE:
                    menu = False

                # Checks if down arrow is pressed
                elif event.key == pg.K_DOWN:
                    if counter < 2:
                        counter += 1

                # Checks if up arrow is pressed
                elif event.key == pg.K_UP:
                    if counter > 0:
                        counter -= 1

                # Checks what is selected
                if counter == 0:
                    selected = "start"
                elif counter == 1:
                    selected = "help"
                elif counter == 2:
                    selected = "quit"

                # Checks if the return key is pressed and acts on it
                if event.key == pg.K_RETURN:
                    if selected == "start":
                        menu = False
                        editor_mode()
                    if selected == "help":
                        menu = False
                    if selected == "quit":
                        menu = False

        # Main menu UI
        # Fills screen
        SCREEN.fill(BLACK)

        # Sets titles and main menu options
        title = text_format("Universum - Sim", font, 90, RED)
        if selected == "start":
            text_start = text_format("START", font, 75, GREEN)
        else:
            text_start = text_format("START", font, 75, WHITE)
        if selected == "help":
            text_help = text_format("HELP", font, 75, GREEN)
        else:
            text_help = text_format("HELP", font, 75, WHITE)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, GREEN)
        else:
            text_quit = text_format("QUIT", font, 75, WHITE)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        help_rect = text_help.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        SCREEN.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
        SCREEN.blit(text_start, (SCREEN_WIDTH / 2 - (start_rect[2] / 2), 300))
        SCREEN.blit(text_help, (SCREEN_WIDTH / 2 - (help_rect[2] / 2), 380))
        SCREEN.blit(text_quit, (SCREEN_WIDTH / 2 - (quit_rect[2] / 2), 460))

        # Update screen and set fps as well as title
        pg.display.update()
        clock.tick(FPS)
        pg.display.set_caption("Planetary Simulation")


def editor_mode():
    """This intializes the mode where you can create Planets and such.
    And drag them around and delete them again"""
    global CIRCLE_RADIUS#
    SCREEN.fill(BLACK)
    objects, radius = [], []
    selected = None
    edit = True

    while edit:
        for event in pg.event.get():
            # Checks if the user presses the 'X' or closes the window
            if event.type == QUIT:
                edit = False

            # Checks if the user presses a key
            elif event.type == KEYDOWN:
                # Closes the window if 'esc' is pressed
                if event.key == pg.K_ESCAPE:
                    edit = False

            # Checks for mouse button press
            elif event.type == MOUSEBUTTONDOWN:
                # Checks if it is the left mouse button
                if event.button == 1:
                    action = "create"
                    objects.append(pg.Rect(event.pos[0], event.pos[1], BLOCK_SIZE, BLOCK_SIZE))
                    radius.append(CIRCLE_RADIUS)

                # Checks if it is the middle mouse button
                elif (event.button == 2) or (event.button == 3):
                    for i, o in enumerate(objects):
                        # Pythagoras a^2 + b^2 = c^2
                        dx = o.centerx - event.pos[0]
                        dy = o.centery - event.pos[1]
                        distance_square = dx ** 2 + dy ** 2

                        # Checks the distance between the cursor and the circle
                        if distance_square <= CIRCLE_RADIUS ** 2:
                            selected = i
                            selected_offset_x = o.x - event.pos[0]
                            selected_offset_y = o.y - event.pos[1]

                    # Checks which button is pressed and adjusts the action
                    if event.button == 2:
                        action = "move"
                    if event.button == 3:
                        action = "destroy"

                # Checks if wheel is turned forward
                elif event.button == 4:
                    if selected is not None:
                        if action == "move":
                            radius[selected] += 35

                # Checks if wheel is turned backward
                elif event.button == 5:
                    if selected is not None:
                        if action == "move":
                            if CIRCLE_RADIUS <= 35:
                                radius[selected] = CIRCLE_RADIUS
                            else:
                                radius[selected] -= 35

            # Checks if mouse button is let loose
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 2:
                    selected = None

            # Checks if mouse is moved
            elif event.type == pg.MOUSEMOTION:
                if selected is not None:
                    if action == "move":
                        objects[selected].x = event.pos[0] + selected_offset_x
                        objects[selected].y = event.pos[1] + selected_offset_y
                    if action == "destroy":
                        del objects[selected]
                        del radius[selected]
                        selected = None

        # Fill screen with black
        SCREEN.fill(BLACK)

        # Main loop UI
        title = text_format("Editing Mode", font, 75, GREEN)
        title_rect = title.get_rect()
        SCREEN.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 0))

        # Draws the circles
        for i, o in enumerate(objects):
            pg.draw.circle(SCREEN, RED, o.center, radius[i])

        # Updates the screen
        pg.display.update()

        # Sets the fps
        clock.tick(FPS)


def main_loop():
    """This is the main loop of the program that simulates the planets movement"""
    # Defines game state
    is_running = True


if __name__ == "__main__":
    # Initializes pygame
    pg.init()

    # Runs the main menu
    main_menu()

    # Quits pygame
    pg.quit()
