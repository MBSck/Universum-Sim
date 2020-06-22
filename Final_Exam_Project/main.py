import sys, os
import pygame as pg

# Selects the files from different folders to be included
sys.path.append(os.path.abspath("scenes"))
sys.path.append(os.path.abspath("assets"))
sys.path.append(os.path.abspath("functio_nality"))

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

if __name__ == "__main__":
    # Initializes pygame
    pg.init()

    # Fill the background of the screen
    SCREEN.fill(BLACK)

    # Runs the main menu
    menu.main_menu()

    # Quits pygame
    pg.quit()
