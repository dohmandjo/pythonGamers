import os
import arcade
import random

"""
    Any variable that remains unchanged through the course of the game should be set here.
    Suggestions are things like player movement speeds, gravity, and file paths.
    In Python semantics, all constant variables are FULL_CAPS_AND_SNAKE_CASE.
"""

WINDOW_TITLE = "Game name goes here"

STARTING_LEVEL = 0

PLAYER_IMAGES = ["res/miner.png", "res/miner-run.png"]
PLAYER_CONTROLS = [arcade.key.W, arcade.key.S, arcade.key.D, arcade.key.A]
PLAYER_SPEED = 10
PLAYER_ACCEL = 1

DEFAULT_SETTINGS = \
'''
"""
    This file contains per-device settings. The default values are stored in `constants.py`.
"""
monitor = 0 # Which display to place window on.
windowed_width = 1280
windowed_height = 720
fullscreen = False
'''
