import sys
import pygame as pg
from pygame.locals import *
import solarsystem as solar
import menu
from utility import *


def editor_mode():
    """This intializes the mode where you can create Planets and such.
    And drag them around and delete them again"""
    global CIRCLE_RADIUS, object_counter
    SCREEN.fill(BLACK)
    objects, radius = [], []
    selected, action = None, None
    edit = True
    # Create solar system
    ss = solar.SolarSystem()

    while edit:
        for event in pg.event.get():
            # Checks if the user presses the 'X' or closes the window
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            # Checks if the user presses a key
            elif event.type == KEYDOWN:
                # Closes the window if 'esc' is pressed
                if event.key == pg.K_ESCAPE:
                    edit = False
                    menu.main_menu()
                    pg.display.quit()

            # Checks for mouse button press
            elif event.type == MOUSEBUTTONDOWN:
                # Checks if object is selected, returns None if not
                selected = mouse_collison(objects, radius)[0]
                # Checks if it is the left mouse button
                if event.button == 1:
                    if selected is None:
                        # Checks if number of planet under max number
                        if object_counter < max_object_number:
                            object_counter += 1
                            objects.append(pg.Rect(event.pos[0], event.pos[1], BLOCK_SIZE, BLOCK_SIZE))
                            radius.append(CIRCLE_RADIUS)
                            # Creates a new planet object if object is created
                            ss.add_planet(solar.planets.Planet("Earth", 10, CIRCLE_RADIUS, event.pos[0], event.pos[1]))
                        else:
                            # Display some error message
                            ...

                # Checks if it is the middle mouse button
                elif event.button == 2:
                    action = "move"

                # Checks if right mouse button is pressed
                elif event.button == 3:
                    if selected is not None:
                        object_counter -= 1
                        del objects[selected]
                        del radius[selected]
                        selected = None

            # Checks if mouse button is let loose
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 2:
                    action = None
                    selected = None

            # Checks if mouse is moved
            elif event.type == pg.MOUSEMOTION:
                if selected is not None:
                    if action == "move":
                        objects[selected].x = event.pos[0] + mouse_collison(objects, radius)[1]
                        objects[selected].y = event.pos[1] + mouse_collison(objects, radius)[2]
            """
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
            """

        # Fill screen with black
        SCREEN.fill(BLACK)

        # Editor UI
        # Sets the text of the non interactable UI elements
        title = text_format("Editing Mode", font, 90, GREEN)

        # Gets the game elements of the non interactable UI
        title_rect = title.get_rect()

        # Sets the position of the non interactable UI elements
        SCREEN.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))

        # Draws the circles
        for i, o in enumerate(objects):
            pg.draw.circle(SCREEN, RED, o.center, radius[i])

        # Updates the screen
        pg.display.update()

        # Sets the fps
        clock.tick(FPS)


def simulation_mode():
    """This is the main loop of the program that simulates the planets movement"""
    # Defines game state
    is_running = True


