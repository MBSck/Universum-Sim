# Useful tools for calculation


def verlet_algorithm(position: int, velocity: int, acceleration: int, dt: int = 0.5):
    """This calculats the second order Taylor solution to the newton DGLs"""
    # Maybe use scipy.integrate to solve newton DGLs

    position = position - velocity * dt + (acceleration * (dt**2) * 0.5)
    velocity = velocity + acceleration * dt

    return position, velocity



