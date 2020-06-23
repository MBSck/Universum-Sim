import sys, os
import pygame as pg

# Selects the files from different folders to be included
sys.path.append(os.path.abspath("scenes"))
sys.path.append(os.path.abspath("assets"))
sys.path.append(os.path.abspath("functionality"))

import menu
from variables import *


"""This is a planet creating tool that leads to a functioning solar system, add some future features like
black holes and such"""

# Startbedigungen für planeten z.B. mit Pfeil in Richtung usw.
# Sollen sich gravitationstechnisch richtig verhalten
# Matrix method?

# Make objects not being able to leave the screen via drag and also not bigger, add options for bigger screen size
# Make objects not being able to be created inside another object
# Make objects be created at tip of cursor not in the middle


def main(self, starting_scene, screen=SCREEN, fps=FPS):
    """Runs the scene"""
    pg.init()

    active_scene = starting_scene

    while active_scene is not None:
        pressed_keys = pg.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pg.event.get():
            quit_attempt = False
            if event.type == QUIT:
                quit_attempt = True
            elif event.type == KEYDOWN:
                alt_pressed = pressed_keys[K_LALT] or \
                    pressed_keys[K_RALT]
                if event.key == K_ESCAPE:
                    quit_attempt = True
                elif event.key == K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)

        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.render(screen)

        pg.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    # Initializes pygame
    pg.init()

    # Fill the background of the screen
    SCREEN.fill(BLACK)

    # Runs the main menu
    menu.main_menu()

    # Quits pygame
    pg.quit()
