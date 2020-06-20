import sys
import pygame as pg


# Selects the files from different folders to be included
sys.path.append("/home/marten/PycharmProjects/Python_Class_Project/Final_Exam_Project/scenes")
sys.path.append("/home/marten/PycharmProjects/Python_Class_Project/Final_Exam_Project/assets")

import menu
from utility import *


"""This is a planet creating tool that leads to a functioning solar system, add some future features like
black holes and such"""

# Startbedigungen für planeten z.B. mit Pfeil in Richtung usw.

# Sollen sich gravitationstechnisch richtig verhalten

# Make main menu and editor function so that you can create new planets and destroy them and soo forth and drag them
# around

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
