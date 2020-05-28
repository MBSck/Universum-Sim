import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image

"""Rules: 1. If a cell is ON and has fewer than two ON neighbors it turns OFF -> Underpopulation
          2. If a cell is ON and has two or three neighbors that are ON, it remains ON -> Stasis
          3. If a cell is ON and has more than three neighbors it turns OFF -> Overpopulation
          4. If a cell is OFF and has exactly three-neighbors that are on, it turns ON -> Reproduction
          """


def evolution(evolution_param, state):
    if evolution_param == 0:
        plt.imshow(state)
        pict = Image.fromarray(state)
        pict.save(f"Pictures/Game_of_Life_end.png")
    else:
        for i in range(evolution_param):
            new_state = state.copy()

            for i in range(0, matrix_size-1):
                for j in range(0, matrix_size-1):
                    if evolution_steps > matrix_size:
                        new_state[i][j] = 0
                    else:
                        environment = state[i][j-1] + state[i][j+1] + state[i+1][j] + state[i-1][j] +\
                                state[i+1][j+1] + state[i+1][j-1] + state[i-1][j+1] + state[i-1][j-1]

                        if state[i][j] == T:
                            if (environment < 2) or (environment > 3):
                                new_state[i][j] = F
                        else:
                            if environment == 3:
                                new_state[i][j] = T

            state = new_state.copy()
            pict = Image.fromarray(state)
            counter = 0
            pict.save(f"Pictures/Game_of_Life_{counter+1}.png")


evolution_steps = 200
matrix_size = 300

T, F = 1, 0
starting_state = np.random.choice([T, F], size=(matrix_size, matrix_size))
plt.imshow(starting_state, cmap=plt.get_cmap("Greys"))
plt.show()
pict = Image.fromarray(starting_state)
pict.save("Game_of_Life_start.png")

evolution(evolution_steps, starting_state)

"""Code works but good method for output is still required"""








