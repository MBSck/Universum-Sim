import tools

class Simulation(tools.SceneBase):
    pass

def simulation_mode():
    """This is the main loop of the program that simulates the planets movement"""
    # Defines game state
    SCREEN.fill(BLACK)
    is_simulating = True
    ss = solar.SolarSystem()

    while is_simulating:
        for event in pg.event.get():
            # Checks if the user presses the 'X' or closes the window
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            # Checks if the user presses a key
            elif event.type == KEYDOWN:
                # Closes the window if 'esc' is pressed
                if event.key == pg.K_ESCAPE:
                    is_simulating = False
                    menu.main_menu()
                    pg.display.quit()

                # For testing and debugging, toggles the simulation
                if event.key == K_1:
                    is_simulating = False
                    editor_mode()
                    break

        # Calculates the paths the planets take
        time.sleep(1)
        ss.planetary_positions()
        ss.update()

        # Fill screen with black
        SCREEN.fill(BLACK)

        # Simulation UI
        # Sets the text of the non interactable UI elements
        title = tools.text_format("Simulation", 90, RED)

        # Gets the game elements of the non interactable UI
        title_rect = title.get_rect()

        # Sets the position of the non interactable UI elements
        SCREEN.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))

        # Draws the circles
        for i in ss.planets_list:
            pg.draw.circle(SCREEN, RED, i.rect.center, i.radius)

        # Updates the screen
        pg.display.update()

        # Sets the fps
        clock.tick(FPS)