import pygame as pg
from pygame.locals import *
from variables import *
import tools
import editor, helper, options


class MainMenu(tools.SceneBase):
    """Class that creates the main menu screen"""
    def __init__(self):
        tools.SceneBase.__init__(self)

        # Sets the counter
        self.counter = 0
        self.selection = {0: "start", 1: "help",
                          2: "options", 3: "quit"}

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == KEYDOWN:

                # Checks if down arrow is pressed
                if event.key == pg.K_DOWN:
                    if self.counter < 3:
                        self.counter += 1

                # Checks if up arrow is pressed
                elif event.key == pg.K_UP:
                    if self.counter > 0:
                        self.counter -= 1

    def update(self):
        pass

    def render(self,  screen=SCREEN, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT):
        # Fills screen
        screen.fill(BLACK)

        # Sets titles and main menu options
        title = tools.text_format("Universum - Sim", 90, RED)
        if self.selection[self.counter] == "start":
            text_start = tools.text_format("START", 75, GREEN)
        else:
            text_start = tools.text_format("START", 75, WHITE)
        if self.selection[self.counter] == "help":
            text_help = tools.text_format("HELP", 75, GREEN)
        else:
            text_help = tools.text_format("HELP", 75, WHITE)
        if self.selection[self.counter] == "options":
            text_options = tools.text_format("OPTIONS", 75, GREEN)
        else:
            text_options = tools.text_format("OPTIONS", 75, WHITE)
        if self.selection[self.counter] == "quit":
            text_quit = tools.text_format("QUIT", 75, GREEN)
        else:
            text_quit = tools.text_format("QUIT", 75, WHITE)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        help_rect = text_help.get_rect()
        options_rect = text_options.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_help, (screen_width / 2 - (help_rect[2] / 2), 380))
        screen.blit(text_options, (screen_width / 2 - (options_rect[2] / 2), 460))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 540))


