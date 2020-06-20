import sys
import pygame as pg
import menu
from pygame.locals import *
from utility import *


def help_menu():
    """This is the help, which explains how to use the simulator"""
    helper = True
    general_pos, editor_pos = 240, 480
    left_pos = 300

    while helper:
        for event in pg.event.get():
            # Checks if the user presses the 'X' or closes the window
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            # Checks if the user presses a key
            elif event.type == KEYDOWN:
                # Closes the window if 'esc' is pressed
                if event.key == pg.K_ESCAPE:
                    helper = False
                    menu.main_menu()
                    pg.display.quit()
        # Help UI
        # Fills screen
        SCREEN.fill(BLACK)

        # Sets titles UI
        title = text_format("Help", font, 90, GREEN)
        general = text_format("General:", font, 75, GREEN)
        editor = text_format("Editor:", font, 75, GREEN)

        # Sets text UI
        escape = text_format("Use escape to go back to main menu", font, 50, GREEN)
        info_mouse_left = text_format("Left click creates object", font, 50, GREEN)
        info_mouse_middle = text_format("Middle click and hold drags object", font, 50, GREEN)
        info_mouse_right = text_format("Right click removes object", font, 50, GREEN)

        # Sets the UI elements
        title_rect = title.get_rect()
        general_rect = general.get_rect()

        info_left_rect = info_mouse_left.get_rect()
        info_middle_rect = info_mouse_middle.get_rect()
        info_right_rect = info_mouse_right.get_rect()

        # Help Text layout
        SCREEN.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
        SCREEN.blit(general, (left_pos - (general_rect[2] / 2), general_pos))
        SCREEN.blit(editor, (left_pos - (general_rect[2] / 2), editor_pos))

        SCREEN.blit(escape, (SCREEN_WIDTH / 2 - (info_middle_rect[2] / 2), general_pos + 130))
        SCREEN.blit(info_mouse_left, (SCREEN_WIDTH / 2 - (info_left_rect[2] / 2), editor_pos + 130))
        SCREEN.blit(info_mouse_middle, (SCREEN_WIDTH / 2 - (info_middle_rect[2] / 2), editor_pos + 260))
        SCREEN.blit(info_mouse_right, (SCREEN_WIDTH / 2 - (info_right_rect[2] / 2), editor_pos + 390))

        # Update screen and set fps as well as title
        pg.display.update()

        # Sets the fps time
        clock.tick(FPS)
