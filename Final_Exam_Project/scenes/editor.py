import Final_Exam_Project.functionality.solarsystem as solar
import Final_Exam_Project.assets.tools as tools
from Final_Exam_Project.scenes import simulation
from Final_Exam_Project.assets.variables import *

# Think about button usability and about scaling of all the UI elements, with Screen size
# Implement inelastic collision


class Editor(tools.SceneBase):
    """This initializes the mode where you can create Planets and such.
    And drag them around and delete them again"""
    def __init__(self):
        tools.SceneBase.__init__(self)

        # Create solar system
        self.ss = solar.SolarSystem()

        # Create variables
        self.selected = None
        self.action = None

        # Initializes the editor menu
        self.menu = tools.SelectionMenu()

    def process_input(self, events, pressed_keys):
        for event in events:

            # Checks for mouse button press
            if event.type == pg.MOUSEBUTTONDOWN:
                # Gets the mouse position
                mouse_pos = event.pos

                # Checks if object is selected, returns None if not
                self.selected = tools.mouse_collison(self.ss.planets_list)[0]

                # Checks if it is the left mouse button
                if event.button == 1:
                    # Checks if collision with button is given
                    if self.menu.start_stop_button.collidepoint(mouse_pos[0], mouse_pos[1]):
                        self.switch_to_scene(simulation.Simulation())

                    # Resets the Solar system planet list
                    elif self.menu.reset_button.collidepoint(mouse_pos[0], mouse_pos[1]):
                        self.ss.reset()

                    elif self.selected is None:
                        # Creates a new object and adds it to the solar system
                        self.ss.add_planet(solar.planets.Planet("Earth", 1e24, mouse_pos[0], mouse_pos[1]))

                    else:
                        # Display some error message
                        ...

                # Checks if it is the middle mouse button
                elif event.button == 2:
                    self.action = "move"

                # Checks if right mouse button is pressed
                elif event.button == 3:
                    if self.selected is not None:
                        self.ss.remove_planet(self.selected)
                        self.selected = None

            # Checks if mouse button is let loose
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 2:
                    self.action = None
                    self.selected = None

            # Checks if mouse is moved
            elif event.type == pg.MOUSEMOTION:
                # Gets the mouse position
                mouse_pos = event.pos

                if self.selected is not None:
                    # Does not work right now
                    if self.action == "move":
                        self.ss.get_planet(self.selected).pos_x = \
                            mouse_pos[0] + tools.mouse_collison(self.ss.planets_list)[1]
                        self.ss.get_planet(self.selected).pos_y = \
                            mouse_pos[1] + tools.mouse_collison(self.ss.planets_list)[2]

    def update(self):
        ...

    def render(self, screen):
        # Editor UI
        # Fill screen with black
        screen.fill(BLACK)

        # Sets the text of the non interaction UI elements
        title = tools.text_format("Editing Mode", 90, GREEN)

        # Gets the game elements of the non interaction UI
        title_rect = title.get_rect()

        # Sets the position of the non interaction UI elements
        screen.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))

        # Draws the start and reset buttons
        self.menu.draw_button(SCREEN, self.menu.start_stop_button, GREEN, "START", self.menu.start_pos[1])
        self.menu.draw_button(SCREEN, self.menu.reset_button, GREEN, "RESET", self.menu.reset_pos[1], 1400)

        # Draws the circles
        for i in self.ss.planets_list:
            pg.draw.circle(screen, i.color, i.rect.center, i.radius)

        # Updates the screen
        pg.display.update()

        # Sets the fps
        clock.tick(FPS)


"""
# Code for resizing objects, adapt later on
# Checks if mousewheel is scrolled
elif event.type == pg.MOUSEWHEEL:
    # Checks if wheel is turned upward
    if (event.wheel.y > 0) or (event.wheel.y < 0):
        selected = mouse_collison(objects, radius)[0]
        if selected is not None:
            radius[selected] += 35

    # Checks if wheel is turned downward
        if event.wheel < 0:
            if selected is not None:
                if radius[selected] <= 35:
                    radius[selected] = CIRCLE_RADIUS
                else:
                    radius[selected] -= 35
"""
