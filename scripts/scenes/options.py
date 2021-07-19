from assets.variables import *
import assets.tools as tools


class Options(tools.SceneBase):
    """Options menu to change screen resolution and different stuff"""

    def __init__(self) -> None:
        """Initializes class attributes"""

        tools.SceneBase.__init__(self)

    def process_input(self, events, pressed_keys) -> None:
        """Handles input"""

        ...

    def update(self) -> None:
        """Updates scene"""

        ...

    def render(self, screen) -> None:
        """Renders option's UI"""

        screen.fill(BLACK)
        ...
