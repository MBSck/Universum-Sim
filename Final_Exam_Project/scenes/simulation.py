import Final_Exam_Project.functionality.solarsystem as solar
import Final_Exam_Project.assets.tools as tools
from Final_Exam_Project.scenes import menu, editor
from Final_Exam_Project.assets.variables import *

# Make Reset button for simulation
# Make two modes mass addition for planets and also
# Add lines to planets so movement is easily seen


class Simulation(tools.SceneBase):
    """This class simulates the planets movement"""
    def __init__(self):
        tools.SceneBase.__init__(self)

        # Reinitializes the solar system class
        self.ss = solar.SolarSystem()

    def process_input(self, events, pressed_keys):
        for event in events:

            # Checks if the user presses a key
            if event.type == pg.KEYDOWN:

                # For testing and debugging, toggles the simulation
                if event.key == pg.K_1:
                    self.switch_to_scene(editor.Editor())

        # Calculates the paths the planets take
        self.ss.planetary_positions()
        self.ss.update()

    def update(self):
        ...

    def render(self, screen):
        # Fill screen with black
        screen.fill(BLACK)

        # Simulation UI
        # Sets the text of the non interactable UI elements
        title = tools.text_format("Simulation", 90, RED)

        # Gets the game elements of the non interactable UI
        title_rect = title.get_rect()

        # Sets the position of the non interactable UI elements
        screen.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))

        # Draws the circles
        for i in self.ss.planets_list:
            pg.draw.circle(screen, RED, i.rect.center, i.radius)
