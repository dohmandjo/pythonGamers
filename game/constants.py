import os
import arcade
import random

"""
    Any variable that remains unchanged through the course of the game should be set here.
    Suggestions are things like player movement speeds, gravity, and file paths.
    In Python semantics, all constant variables are FULL_CAPS_AND_SNAKE_CASE.
"""

SETTINGS_FILE = "settings.json"

WINDOW_TITLE = "Me, Mineself, and I"

PLAYER_IMAGES = ["res/miner.png", "res/miner-run.png"]
PLAYER_CONTROLS = [[arcade.key.W, arcade.key.UP], 
                   [arcade.key.S, arcade.key.DOWN], 
                   [arcade.key.D, arcade.key.RIGHT], 
                   [arcade.key.A, arcade.key.LEFT]]

FLOOR_IMAGES = ["res/stage/platform1.png", "res/stage/platform2.png","res/stage/platform3.png", "res/stage/platform4.png", "blank"]
FLOOR_HEIGHT = 64
RUN_LENGTH = 12500
PLATFORM_HEIGHTS = (264, 464, 664)

LAVA_IMAGES = ["res/stage/lava-column.png", "res/stage/lava-ground-erupt.png"]
WALL_HEIGHT = 1064

GEM_IMAGES = ["res/drop/black-gem.png", "res/drop/red-gem.png", "res/drop/blue-gem.png", "res/drop/yellow-gem.png", "res/drop/green-gem.png", "res/drop/rock.png", "res/drop/coal.png"]
SCORE_DISPLAY = 23

STARTING_LEVEL = 0

MUSIC_VOLUME = 1

DEFAULT_SETTINGS = \
'''
{
    "monitor": 0,
    "windowed_width": 1280,
    "windowed_height": 720,
    "fullscreen": "False"
}
'''