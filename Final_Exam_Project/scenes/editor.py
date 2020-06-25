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
        self.menu = SelectionMenu()

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
                        # Selects planet for variable change if one already exists at this point
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
        # Gets the selected planets values and renders them on the screen
        if self.selected is not None:
            # self.menu.draw_variable_input(SCREEN, self.ss.get_planet(self.selected_planet))
            print(self.ss.get_planet(self.selected), end=", ")

            # Does not work as for some reason if you click on planet it gets looped

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
        self.menu.draw_menu(SCREEN)

        # Draws the circles
        for i in self.ss.planets_list:
            pg.draw.circle(screen, i.color, i.rect.center, i.radius)

        # Updates the screen
        pg.display.update()

        # Sets the fps
        clock.tick(FPS)


class SelectionMenu:
    """Implements selection menu to change the values of the planets"""
    def __init__(self):
        self.start_pos = (150, 950)
        self.stop_pos = (150, 950)
        self.reset_pos = (1550, 950)

        # Sets the position of the buttons
        self.start_stop_button = pg.Rect(self.start_pos[0], self.start_pos[1], 200, 50)
        self.reset_button = pg.Rect(self.reset_pos[0], self.reset_pos[1], 200, 50)

    def draw_button(self, screen, button_rect, color, text, pos_y, offset_x=0, offset_y=1.5):
        """Draw button with text on it that is in black"""
        # Draws the button, gets the text and then a possible offsets to center text on button position
        pg.draw.rect(screen, color, button_rect)
        button_text = tools.text_format(text, text_size=45, text_color=BLACK)
        button_rect = button_text.get_rect()
        screen.blit(button_text, (button_rect[2] + offset_x, pos_y - offset_y))

    def draw_menu(self, screen):
        """Draws the menu elements"""
        # Draws the menus borders
        pg.draw.rect(screen, GREEN, pg.Rect(10, 10, 575, 230), 10)

        # Sets the title and text of the menu
        menu_title = tools.text_format("Stellar Object Menu", 30, GREEN)
        menu_name = tools.text_format("Name:", 20, GREEN)
        menu_mass = tools.text_format("Mass:", 20, GREEN)
        menu_density = tools.text_format("Density:", 20, GREEN)
        menu_radius = tools.text_format("Radius:", 20, GREEN)
        menu_velocity_x = tools.text_format("Velocity X:", 20, GREEN)
        menu_velocity_y = tools.text_format("Velocity Y:", 20, GREEN)

        # Gets the rects
        menu_title_rect = menu_title.get_rect()
        menu_name_rect = menu_mass.get_rect()
        menu_mass_rect = menu_mass.get_rect()
        menu_radius_rect = menu_radius.get_rect()
        menu_density_rect = menu_density.get_rect()

        # Variable that sets all of the values on the leftbound
        LEFTBOUND = (SCREEN_WIDTH / 30 - (menu_name_rect[2] / 2))

        # Displays the text
        screen.blit(menu_title, (SCREEN_WIDTH / 6.3 - (menu_title_rect[2] / 2),
                                 SCREEN_HEIGHT / 4.8 - (menu_title_rect[2] / 2)))
        screen.blit(menu_name, (LEFTBOUND, SCREEN_HEIGHT / 10.2 - (menu_name_rect[2] / 2)))
        screen.blit(menu_mass, (LEFTBOUND, SCREEN_HEIGHT / 8.2 - (menu_mass_rect[2] / 2)))
        screen.blit(menu_radius, (LEFTBOUND, SCREEN_HEIGHT / 6.5 - (menu_radius_rect[2] / 2)))
        screen.blit(menu_density, (LEFTBOUND, SCREEN_HEIGHT / 5.4 - (menu_density_rect[2] / 2)))
        screen.blit(menu_velocity_x, (LEFTBOUND, SCREEN_HEIGHT / 5.1 - (menu_name_rect[2] / 2)))
        screen.blit(menu_velocity_y, (LEFTBOUND, SCREEN_HEIGHT / 4.5 - (menu_name_rect[2] / 2)))

    def draw_variable_input(self, screen, planet):
        """Displays the changeable variables of the object"""
        # Sets the rect title via the planets data
        input_name = tools.text_format(str(planet.name), 20, GREEN)
        input_mass = tools.text_format(str(planet.mass), 20, GREEN)
        input_radius = tools.text_format(str(planet.radius), 20, GREEN)
        input_density = tools.text_format(str(planet.density), 20, GREEN)
        input_velocity_x = tools.text_format(str(planet.v_x), 20, GREEN)
        input_velocity_y = tools.text_format(str(planet.v_y), 20, GREEN)

        # Gets the rects
        input_name_rect = input_name.get_rect()
        input_mass_rect = input_mass.get_rect()
        input_radius_rect = input_radius.get_rect()
        input_density_rect = input_density.get_rect()
        input_velocity_x_rect = input_velocity_x.get_rect()
        input_velocity_y_rect = input_velocity_y.get_rect()

        # Variable that sets all of the values on the leftbound
        RIGHTBOUND = (SCREEN_WIDTH / 15 - (input_name_rect[2] / 2))

        # Displays the text
        screen.blit(input_name, (RIGHTBOUND, SCREEN_HEIGHT / 10.2 - (input_name_rect[2] / 2)))
        screen.blit(input_mass, (RIGHTBOUND, SCREEN_HEIGHT / 8.2 - (input_mass_rect[2] / 2)))
        screen.blit(input_radius, (RIGHTBOUND, SCREEN_HEIGHT / 6.5 - (input_radius_rect[2] / 2)))
        screen.blit(input_density, (RIGHTBOUND, SCREEN_HEIGHT / 5.4 - (input_density_rect[2] / 2)))
        screen.blit(input_velocity_x, (RIGHTBOUND, SCREEN_HEIGHT / 5.1 - (input_velocity_x_rect[2] / 2)))
        screen.blit(input_velocity_y, (RIGHTBOUND, SCREEN_HEIGHT / 4.5 - (input_velocity_y_rect[2] / 2)))

    def update(self):
        """Updates the menu screen"""
        ...
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
