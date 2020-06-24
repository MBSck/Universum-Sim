import Final_Exam_Project.functionality.solarsystem as solar
import Final_Exam_Project.assets.tools as tools
from Final_Exam_Project.scenes import editor
from Final_Exam_Project.assets.variables import *

# Make Reset button for simulation
# Make two modes if collide mass addition for planets and also
# Add lines to planets so movement is easily seen


class Simulation(tools.SceneBase):
    """This class simulates the planets movement"""
    def __init__(self):
        tools.SceneBase.__init__(self)

        # Re-initializes the solar system class
        self.ss = solar.SolarSystem()

        # Initializes the editor menu
        self.menu = tools.SelectionMenu()

    def process_input(self, events, pressed_keys):
        for event in events:

            # Checks if mousbutton is pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # Checks if it is the left mouse button
                if event.button == 1:
                    # Checks if collision with button is given
                    if self.menu.start_stop_button.collidepoint(mouse_pos[0], mouse_pos[1]):
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

        # Draw quit button
        self.menu.draw_button(SCREEN, self.menu.start_stop_button, RED, "STOP", self.menu.stop_pos[1], 50)

        # Draws the circles
        for i in self.ss.planets_list:
            pg.draw.circle(screen, i.color, i.rect.center, i.radius)
            # i.draw_trace(screen)


