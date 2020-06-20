import sys
import pygame as pg
from pygame.locals import *

# Selects the files from different folders to be included
sys.path.append("/home/marten/PycharmProjects/Python_Class_Project/Final_Exam_Project/assets")

# Import the utility
from utility import *


def editor_mode():
    """This intializes the mode where you can create Planets and such.
    And drag them around and delete them again"""
    global CIRCLE_RADIUS
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
                selected = mouse_collison(objects, radius)[0]
                # Checks if it is the left mouse button
                if event.button == 1:
                    if selected is None:
                        action = "create"
                        objects.append(pg.Rect(event.pos[0], event.pos[1], BLOCK_SIZE, BLOCK_SIZE))
                        radius.append(CIRCLE_RADIUS)

                # Checks if it is the middle mouse button
                elif event.button == 2:
                    action = "move"

                # Checks if right mouse button is pressed
                elif event.button == 3:
                    if selected is not None:
                        del objects[selected]
                        del radius[selected]
                        selected = None

            # Checks if mouse button is let loose
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 2:
                    selected = None

            # Checks if mouse is moved
            elif event.type == pg.MOUSEMOTION:
                if selected is not None:
                    if action == "move":
                        objects[selected].x = event.pos[0] + mouse_collison(objects, radius)[1]
                        objects[selected].y = event.pos[1] + mouse_collison(objects, radius)[2]

            # Checks if mousewheel is scrolled
            elif event.type == pg.MOUSEWHEEL:
                # Checks if wheel is turned upward
                if (event.wheel.y > 0) or (event.wheel.y < 0):
                    selected = mouse_collison(objects, radius)[0]
                    if selected is not None:
                        radius[selected] += 35

                # Checks if wheel is turned downward
                    if event.wheel < 0:
                        if selected is not None:
                            if radius[selected] <= 35:
                                radius[selected] = CIRCLE_RADIUS
                            else:
                                radius[selected] -= 35

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


def simulation():
    """This is the main loop of the program that simulates the planets movement"""
    # Defines game state
    is_running = True
