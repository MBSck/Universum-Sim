import time
import pygame as pg
import tools
import solarsystem as solar
import menu, editor


class Simulation(tools.SceneBase):
    def __init__(self):
        tools.SceneBase.__init__(self)

        # Reinitializes the solar system class
        self.ss = solar.SolarSystem()

    def process_input(self, events, pressed_keys):
        for event in events:

            # Checks if the user presses a key
            if event.type == pg.KEYDOWN:

                # Closes the window if 'esc' is pressed
                if event.key == pg.K_ESCAPE:
                    self.switch_to_scene(menu.MainMenu())

                # For testing and debugging, toggles the simulation
                if event.key == pg.K_1:
                    editor_mode()

        # Calculates the paths the planets take
        time.sleep(1)
        ss.planetary_positions()
        ss.update()

    def update(self):
        time.sleep(0.5)

    def render(self, screen):
        ...

def simulation_mode():
    """This is the main loop of the program that simulates the planets movement"""
    # Defines game state
    SCREEN.fill(BLACK)
    is_simulating = True




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
        for i in ss.planets_list:
            pg.draw.circle(SCREEN, RED, i.rect.center, i.radius)

        # Updates the screen
        pg.display.update()

        # Sets the fps
        clock.tick(FPS)