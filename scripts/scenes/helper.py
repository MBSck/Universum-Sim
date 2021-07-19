from assets.variables import *
import assets.tools as tools
from scenes import menu


class Help(tools.SceneBase):
    """Creates the help menu, which explains how to use the simulator"""

    def __init__(self) -> None:
        """Initialize class attributes"""

        tools.SceneBase.__init__(self)

        self.general_pos, self.editor_pos = 240, 480
        self.left_pos = 300

    def process_input(self, events, pressed_keys) -> None:
        """Handles input"""

        for event in events:
            # Checks if the user presses a key
            if event.type == pg.KEYDOWN:
                # Closes the window if 'esc' is pressed
                if event.key == pg.K_ESCAPE:
                    self.switch_to_scene(menu.MainMenu())

    def update(self) -> None:
        """Updates scene"""

        pass

    def render(self, screen) -> None:
        """Renders the helper's UI"""

        # Fills screen
        screen.fill(BLACK)

        # Sets titles UI
        title = tools.text_format("Help", 90, GREEN)
        general = tools.text_format("General:", 75, GREEN)
        editor = tools.text_format("Editor:", 75, GREEN)

        # Sets text UI
        escape = tools.text_format("Use escape to go back to main menu", 50, GREEN)
        info_mouse_left = tools.text_format("Left click creates object", 50, GREEN)
        info_mouse_middle = tools.text_format("Middle click and hold drags object", 50, GREEN)
        info_mouse_right = tools.text_format("Right click removes object", 50, GREEN)

        # Sets the UI elements
        title_rect = title.get_rect()
        general_rect = general.get_rect()

        info_left_rect = info_mouse_left.get_rect()
        info_middle_rect = info_mouse_middle.get_rect()
        info_right_rect = info_mouse_right.get_rect()

        # Help Text layout
        screen.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
        screen.blit(general, (self.left_pos - (general_rect[2] / 2), self.general_pos))
        screen.blit(editor, (self.left_pos - (general_rect[2] / 2), self.editor_pos))

        screen.blit(escape, (SCREEN_WIDTH / 2 - (info_middle_rect[2] / 2), self.general_pos + 130))
        screen.blit(info_mouse_left, (SCREEN_WIDTH / 2 - (info_left_rect[2] / 2), self.editor_pos + 130))
        screen.blit(info_mouse_middle, (SCREEN_WIDTH / 2 - (info_middle_rect[2] / 2), self.editor_pos + 260))
        screen.blit(info_mouse_right, (SCREEN_WIDTH / 2 - (info_right_rect[2] / 2), self.editor_pos + 390))
