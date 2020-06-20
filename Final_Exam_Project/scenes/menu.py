import sys
import pygame as pg
from pygame.locals import *

import editor

# Selects the files from different folders to be included
sys.path.append("/home/marten/PycharmProjects/Python_Class_Project/Final_Exam_Project/assets")

from utility import *


def main_menu():
    """This is the intro of our program, starting menu"""
    menu = True
    selected = "start"
    counter = 0

    while menu:
        for event in pg.event.get():
            # Checks if the user presses the 'X' or closes the window
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            # Checks for keypress
            if event.type == KEYDOWN:
                # Closes the window if 'esc' is pressed
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

                # Checks if down arrow is pressed
                elif event.key == pg.K_DOWN:
                    if counter < 3:
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
                    selected = "options"
                elif counter == 3:
                    selected = "quit"

                # Checks if the return key is pressed and acts on it
                if event.key == pg.K_RETURN:
                    if selected == "start":
                        menu = False
                        editor.editor_mode()
                        pg.display.quit()
                        break
                    if selected == "help":
                        menu = False
                    if selected == "options":
                        menu = False
                    if selected == "quit":
                        pg.quit()
                        sys.exit()

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
        if selected == "options":
            text_options = text_format("OPTIONS", font, 75, GREEN)
        else:
            text_options = text_format("OPTIONS", font, 75, WHITE)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, GREEN)
        else:
            text_quit = text_format("QUIT", font, 75, WHITE)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        help_rect = text_help.get_rect()
        options_rect = text_options.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        SCREEN.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
        SCREEN.blit(text_start, (SCREEN_WIDTH / 2 - (start_rect[2] / 2), 300))
        SCREEN.blit(text_help, (SCREEN_WIDTH / 2 - (help_rect[2] / 2), 380))
        SCREEN.blit(text_options, (SCREEN_WIDTH / 2 - (options_rect[2] / 2), 460))
        SCREEN.blit(text_quit, (SCREEN_WIDTH / 2 - (quit_rect[2] / 2), 540))

        # Update screen and set fps as well as title
        pg.display.update()
        clock.tick(FPS)
        pg.display.set_caption("Planetary Simulation")