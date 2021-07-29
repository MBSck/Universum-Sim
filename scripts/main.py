from assets.variables import *
from scenes import menu

__version__ = "0.0.1 - Alpha"
__author__ = "Marten Scheuck"

"""This is simulation tool, which generates physical accurate planetary body simulations"""

# TODO: Start options for planets, like speed etc. should be shown visually by arrow into direction
# TODO: Matrix method?
# TODO: Make objects not being able to leave the screen via drag and also not bigger, add options for bigger screen size
# TODO: Make objects be created at tip of cursor not in the middle
# TODO: Maybe make zoom function so that you can see all of the system
# TODO: Fix collision problem of planets if collide, then merge
# TODO: Implement sprite classes into code
# TODO: Change all the positions into relative to screen size, so that it works on lower resolution
# TODO: Computation really slow -> Fix! (Matrix calculation)


def initialize(screen) -> None:
    """Initializes the main pygame functionality and the music

    Parameters:
        screen
            the screen pygame displays on

    Returns:
        None
    """

    # Initializes pygame and the first scene
    pg.init()
    screen.fill(BLACK)

    # Music
    pg.mixer_music.load(os.path.join("assets/music/", rnd.choice(songs)))
    pg.mixer_music.play(-1)
    pg.mixer.music.set_volume(VOLUME)


def check_for_user_input(active_scene, pressed_keys):
    """This is part of the simulations while loop and checks for user input

    Parameters:
        active_scene
            the scene that is active at the moment
        pressed_keys
            the keys pressed by the user

    Returns:
        filtered_events: list
            a list that encompasses all user events
    """

    filtered_events = []

    # Checks if user pressed alt+f4, 'x' or escape
    for event in pg.event.get():
        quit_attempt = False

        # Checks oif key is pressed
        if event.type == pg.KEYDOWN:

            # If 'esc' is pressed either returns to main menu or quits
            if (event.key == pg.K_ESCAPE) and (active_scene != menu.MainMenu()):

                # Switches Scene and resets the SolarSystem
                active_scene.next = menu.MainMenu()
                menu.editor.solar.SolarSystem().reset()

            # If 'alt+F4' is pressed quits
            if event.key == pg.K_F4 and (pressed_keys[pg.K_LALT] or pressed_keys[pg.K_RALT]):
                quit_attempt = True

            # Checks if 'x' on window is pressed
            if event.type == pg.QUIT:
                quit_attempt = True

            # If 'F11' is pressed fullscreen toggles
            if event.key == pg.K_F11:
                pg.display.toggle_fullscreen()

        # Quits if any quit conditions are met and if not takes the events
        if quit_attempt:
            active_scene.terminate()
        else:
            active_scene.append(event)

        return filtered_events


def main(active_scene, screen=SCREEN, fps: int = FPS) -> None:
    """Starts up the simulation and runs the first scene. Contains main game loop

    Parameters:
        active_scene: The active scene, utilizing the respective Scene class
        screen: the screen pygame displays on
        fps (int): The frames per second that are rendered

    Returns:
        None
    """

    # Initialize the pygame settings
    initialize(screen)

    while True:
        # Gets the pressed keys
        pressed_keys = pg.key.get_pressed()

        # Gets user input
        filtered_events = check_for_user_input(active_scene, pressed_keys)

        # Takes User Input, updates the game for any actions and then renders the screen
        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.render(screen=screen)

        # switches to next scene if it changed
        active_scene = active_scene.next

        # Sets the caption of the window
        pg.display.set_caption("Planetary Simulation")

        # Updates the whole display, like pg.display.flip()
        pg.display.update()

        # Sets the games clock
        clock.tick(fps)


if __name__ == "__main__":

    # Start the main game loop
    main(menu.MainMenu())
