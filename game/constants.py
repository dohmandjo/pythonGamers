import os
import arcade
import random

"""
    Any variable that remains unchanged through the course of the game should be set here.
    Suggestions are things like player movement speeds, gravity, and file paths.
    In Python semantics, all constant variables are FULL_CAPS_AND_SNAKE_CASE.
"""

SETTINGS_FILE = "settings.json"

WINDOW_TITLE = "Game name goes here"

PLAYER_IMAGES = ["res/miner.png", "res/miner-run.png"]
PLAYER_CONTROLS = [[arcade.key.W, arcade.key.UP], 
                   [arcade.key.S, arcade.key.DOWN], 
                   [arcade.key.D, arcade.key.RIGHT], 
                   [arcade.key.A, arcade.key.LEFT]]

STARTING_LEVEL = 0

DEFAULT_SETTINGS = \
'''
{
    "monitor": 0,
    "windowed_width": 1280,
    "windowed_height": 720,
    "fullscreen": "False"
}
'''