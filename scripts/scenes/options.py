from assets.variables import *
import assets.tools as tools
from scenes import menu

# TODO: Make fullscreen toggle mechanic work
# TODO: Make settings permanent in some file, cfg or something


class Options(tools.SceneBase):
    """Options menu to change screen resolution and different stuff

    Attributes
    ----------
    counter: int
        keeps track of the user's selection
    sound_settings: dict
        keeps track of different sound volumes
    fullscreen_settings: dict
        has two options either 'Yes' or 'No' that decide on fullscreen- or window-mode
    selection: dict
        uses the counter to get the object of the user's current selection

    Methods
    ----------
    process_input(events, pressed_keys):
        Handles input
    update():
        Updates scene
    render(screen):
        Renders the helper's UI
    """

    def __init__(self) -> None:
        """Initialize class attributes

        Returns
        ----------
        None
        """

        tools.SceneBase.__init__(self)

        # Sets the option's counter
        self.counter = 0

        # Various lists for the selections
        self.sound_settings = {0: ("--------- 0", 0.), 1: ("| | | ------- 25", 0.25),
                               2: ("| | | | | | ----  50", 0.5), 3: ("| | | | | | | | | --  75", 0.75),
                               4: ("| | | | | | | | | | | |  100", 1.)}
        self.fullscreen_settings = {0: "YES", 1: "NO"}

        # Sets the selections
        self.selection = {0: "Sound", 1: "Fullscreen", 2: "Back"}

    def process_input(self, events, pressed_keys) -> None:
        """Handles input

        Parameters
        ----------
        events: int
            the different game events
        pressed_keys: str
            the keys pressed by the user

        Returns
        ----------
        None
        """

        global volume_setting, fullscreen_setting

        for event in events:
            if event.type == pg.KEYDOWN:

                # Checks if down arrow is pressed
                if event.key == pg.K_DOWN:
                    if self.counter < 2:
                        self.counter += 1

                # Checks if up arrow is pressed
                elif event.key == pg.K_UP:
                    if self.counter > 0:
                        self.counter -= 1

                # Checks if left or right arrow is pressed and changes the sound or fullscreen
                if (event.key == pg.K_RIGHT) or (event.key == pg.K_LEFT):
                    if self.selection[self.counter] == "Sound":
                        if (event.key == pg.K_RIGHT) and (volume_setting < 4):
                            volume_setting += 1

                            # sets sound
                            pg.mixer.music.set_volume(self.sound_settings[volume_setting][1])

                        elif (event.key == pg.K_LEFT) and (volume_setting > 0):
                            volume_setting -= 1

                            # sets sound
                            pg.mixer.music.set_volume(self.sound_settings[volume_setting][1])

                    elif self.selection[self.counter] == "Fullscreen":
                        if fullscreen_setting == 0:
                            fullscreen_setting = 1

                        else:
                            fullscreen_setting = 0

                        # pg.display.toggle_fullscreen()

                # Back option returns to main menu
                if (self.selection[self.counter] == "Back") and (event.key == pg.K_RETURN):
                    self.switch_to_scene(menu.MainMenu())

    def update(self) -> None:
        """Updates scene

        Returns
        ----------
        None
        """

        pass

    def render(self, screen) -> None:
        """Renders the option's UI

        Parameters
        ----------
        screen
            the screen pygame displays on

        Returns
        ----------
        None
        """

        screen.fill(BLACK)

        # Sets titles and main menu options
        title = tools.text_format("OPTIONS", 90, RED)
        if self.selection[self.counter] == "Sound":
            text_sound = tools.text_format("SOUND:", 75, GREEN)
            text_sound_bar = tools.text_format(self.sound_settings[volume_setting][0], 75, GREEN)
        else:
            text_sound = tools.text_format("SOUND:", 75, WHITE)
            text_sound_bar = tools.text_format(self.sound_settings[volume_setting][0], 75, WHITE)

        if self.selection[self.counter] == "Fullscreen":
            text_fullscreen = tools.text_format("FULLSCREEN:", 75, GREEN)
            text_fullscreen_setting = tools.text_format(self.fullscreen_settings[fullscreen_setting], 75, GREEN)
        else:
            text_fullscreen = tools.text_format("FULLSCREEN:", 75, WHITE)
            text_fullscreen_setting = tools.text_format(self.fullscreen_settings[fullscreen_setting], 75, WHITE)

        if self.selection[self.counter] == "Back":
            text_back = tools.text_format("BACK", 75, GREEN)
        else:
            text_back = tools.text_format("BACK", 75, WHITE)

        # Gets the rects
        title_rect = title.get_rect()
        sound_rect = text_sound.get_rect()
        fullscreen_rect = text_fullscreen.get_rect()
        back_rect = text_back.get_rect()

        # Main Menu Text
        screen.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_sound, (SCREEN_WIDTH / 2 - (sound_rect[2]) - 100, 300))
        screen.blit(text_sound_bar, (SCREEN_WIDTH / 2 + 50, 300))
        screen.blit(text_fullscreen, (SCREEN_WIDTH / 2 - fullscreen_rect[2] - 100, 400))
        screen.blit(text_fullscreen_setting, (SCREEN_WIDTH / 2 + 50, 400))
        screen.blit(text_back, (SCREEN_WIDTH / 2 - (back_rect[2] / 2), 500))
