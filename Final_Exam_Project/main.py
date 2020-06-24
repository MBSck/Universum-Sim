from Final_Exam_Project.assets.variables import *
from Final_Exam_Project.scenes import menu

"""This is a planet creating tool that leads to a functioning solar system, add some future features like
black holes and such"""

# Start options for planets, like speed etc. should be shown visually by arrow into direction
# Matrix method?

# Make objects not being able to leave the screen via drag and also not bigger, add options for bigger screen size
# Make objects be created at tip of cursor not in the middle
# Maybe make zoom function so that you can see all of the system


def main(starting_scene, screen=SCREEN, fps=FPS):
    """Runs the scenes and is therefore the main game loop"""
    pg.init()
    screen.fill(BLACK)
    active_scene = starting_scene

    while True:
        # Gets the pressed keys
        pressed_keys = pg.key.get_pressed()

        # Event filtering
        filtered_events = []

        # Checks if user pressed alt+f4, 'x' or escape
        for event in pg.event.get():
            quit_attempt = False

            # Checks if 'x' on window is pressed
            if event.type == pg.QUIT:
                quit_attempt = True

            # Checks oif key is pressed
            elif event.type == pg.KEYDOWN:

                # Checks if either the left or right alt key is pressed
                alt_pressed = pressed_keys[pg.K_LALT] or \
                    pressed_keys[pg.K_RALT]

                # If 'esc' is pressed either returns to main menu or quits
                if event.key == pg.K_ESCAPE:
                    # This doesn't work, but why?
                    if active_scene == menu.MainMenu():
                        quit_attempt = True
                    else:
                        # Switches Scene and resets the SolarSystem
                        active_scene.next = menu.MainMenu()
                        menu.editor.solar.SolarSystem().reset()

                # If 'alt+F4' is pressed quits
                elif event.key == pg.K_F4 and alt_pressed:
                    quit_attempt = True

                # If 'F11' is pressed fullscreen toggles on/off
                elif event.key == pg.K_F11:
                    pg.display.toggle_fullscreen()

            # Quits if any quit conditions are met
            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)

        # Updates the scene with new content
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

