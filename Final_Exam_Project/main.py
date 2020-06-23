import sys, os
import pygame as pg

# Import all needed modules for the different submodules
import sys, os

# Selects the files from different folders to be included
sys.path.append(os.path.abspath("scenes"))
sys.path.append(os.path.abspath("assets"))
sys.path.append(os.path.abspath("functionality"))

from assets.variables import *

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


def main(starting_scene, screen=SCREEN, fps=FPS):
    """Runs the scenes and is therefore the main game loop"""
    pg.init()
    SCREEN.fill(BLACK)
    active_scene = starting_scene

    while True:
        pressed_keys = pg.key.get_pressed()

        # Event filtering
        filtered_events = []

        # Checks if user pressed alt+f4, 'x' or escape
        for event in pg.event.get():
            quit_attempt = False

            if event.type == pg.QUIT:
                quit_attempt = True
            elif event.type == pg.KEYDOWN:
                alt_pressed = pressed_keys[pg.K_LALT] or \
                    pressed_keys[pg.K_RALT]
                if event.key == pg.K_F4 and alt_pressed:
                    quit_attempt = True
                elif event.key == pg.K_F11:
                    pg.display.toggle_fullscreen()

            # Quits if any quit conditions are met
            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)

        # Updates the scene with new content
        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.render(screen=SCREEN)

        # switches to next scene if it changed
        active_scene = active_scene.next

        # Sets the caption of the window
        pg.display.set_caption("Planetary Simulation")

        # Updates the whole display, like pg.display.flip()
        pg.display.update()

        # Sets the games clock
        clock.tick(fps)


if __name__ == "__main__":
    main(menu.MainMenu())

