import os
import pygame as pg
import time
import numpy as np
import decimal
import random as rnd
import abc
import sys

"""Implement class that keeps check of colors and globals etc."""

# TODO: Make solarsystem objects accesible via options menu via singleton
# TODO: Temporarly sprite host, make functions into classes and use sprite functionality

# Center the application
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Set screen
SCREEN = pg.display.set_mode((0, 0), pg.FULLSCREEN)

# Implementation for music and setting song that is being played
songs = ["slowmotion.mp3", "newdawn.mp3", "deepblue.mp3"]
currently_playing_song = None
VOLUME = 0.1

# Get screen size
info = pg.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
MAX_RESOLUTION = (info.current_w, info.current_h)

# Set fps and clock
FPS, clock = 60, pg.time.Clock()

# Define colors
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)

# Font
font = "assets/Gameplay.ttf"

# Size of the circles/planets
BLOCK_SIZE = 25
CIRCLE_RADIUS = int(BLOCK_SIZE/2)

# max_number of objects and object_counter
object_counter = 0
objects = []
radius = []

# The gravitational constant in m**3 kg**-1 s**-2
gravitational_constant = 6.67408e-11

# One astronomical unit in meters
au = 149597870.7e03

# Timesteps for integration i=1
TIMESTEP = 0.15

# Set a Pixel to be roughly equal to 1/10 of an au
PIXEL_INCREMENT = 1e08
PIXEL_REAL = au/PIXEL_INCREMENT

# exoplanet and stars list/ web scrape later, whole list and add stars, too!
generic_name_list = ["Spe", "Arkas", "Arion", "Dimidium", "Earth", "Moon", "Mars",
                     "Venus", "Jupiter", "Sun", "Merkur", "Saturn", "Aegir", "Dagon",
                     "Hypatia", "Madriu", "Xolotlan", "Riosar", ]
