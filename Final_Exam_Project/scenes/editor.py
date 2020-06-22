import sys
import pygame as pg
from pygame.locals import *
from variables import *
import tools
import solarsystem as solar
import menu


def editor_mode():
    """This intializes the mode where you can create Planets and such.
    And drag them around and delete them again"""
    global CIRCLE_RADIUS

    SCREEN.fill(BLACK)
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

                # For testing and debugging, toggles the simulation
                if event.key == K_1:
                    edit = False
                    simulation_mode()
                    break

            # Checks for mouse button press
            elif event.type == MOUSEBUTTONDOWN:
                # Gets the mouse position
                mouse_pos = event.pos

                # Checks if object is selected, returns None if not
                selected = tools.mouse_collison(ss.planets_list)[0]

                # Checks if it is the left mouse button
                if event.button == 1:
                    if selected is None:
                        # Creates a new object and adds it to the solar system
                        ss.add_planet(solar.planets.Planet("Earth", 10, mouse_pos[0], mouse_pos[1]))
                    else:
                        # Display some error message
                        ...

                # Checks if it is the middle mouse button
                elif event.button == 2:
                    action = "move"

                # Checks if right mouse button is pressed
                elif event.button == 3:
                    if selected is not None:
                        ss.remove_planet(selected)
                        selected = None

            # Checks if mouse button is let loose
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 2:
                    action = None
                    selected = None

            # Checks if mouse is moved
            elif event.type == pg.MOUSEMOTION:
                # Gets the mouse position
                mouse_pos = event.pos

                if selected is not None:
                    if action == "move":
                        ss.get_planet(selected).rect.x = mouse_pos[0] + tools.mouse_collison(ss.planets_list)[1]
                        ss.get_planet(selected).rect.y = mouse_pos[1] + tools.mouse_collison(ss.planets_list)[2]
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
        title = tools.text_format("Editing Mode", 90, GREEN)

        # Gets the game elements of the non interactable UI
        title_rect = title.get_rect()

        # Sets the position of the non interactable UI elements
        SCREEN.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))

        # Draws the circles
        for i, o in enumerate(ss.planets_list):
            pg.draw.circle(SCREEN, RED, o.rect.center, o.radius)

        # Updates the screen
        pg.display.update()

        # Sets the fps
        clock.tick(FPS)


def simulation_mode():
    """This is the main loop of the program that simulates the planets movement"""
    # Defines game state
    SCREEN.fill(BLACK)
    is_simulating = True
    ss = solar.SolarSystem()

    while is_simulating:

        for event in pg.event.get():
            # Checks if the user presses the 'X' or closes the window
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            # Checks if the user presses a key
            elif event.type == KEYDOWN:
                # Closes the window if 'esc' is pressed
                if event.key == pg.K_ESCAPE:
                    is_simulating = False
                    pg.display.quit()

                # For testing and debugging, toggles the simulation
                if event.key == K_1:
                    is_simulating = False
                    editor_mode()
                    break

        # Fill screen with black
        SCREEN.fill(BLACK)

        # Simulation UI
        # Sets the text of the non interactable UI elements
        title = tools.text_format("Simulation", 90, RED)

        # Gets the game elements of the non interactable UI
        title_rect = title.get_rect()

        # Sets the position of the non interactable UI elements
        SCREEN.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))

        # Draws the circles
        for i, o in enumerate(ss.planets_list):
            pg.draw.circle(SCREEN, RED, o.rect.center, o.radius)

        # Updates the screen
        pg.display.update()

        # Sets the fps
        clock.tick(FPS)
