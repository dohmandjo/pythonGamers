""" 
    [GAME TITLE HERE]
    Filesystem:

        /
            Root of game data, contains `main.py` and `README.md`

        /game
            Contains everything engine related. Entity data, behavior, anything hard-coded

            /game/engine
                Components of the game engine itself, the director, map loader, physics, etc.
                Files:
                    arcade_engine.py    |       Main portion of the engine, coordinates the calling of other functions.
                    physics.py          |       Handles things like gravity, collision, reflection, and player movement.

            /game/entity
                Components of the various entities used by the game. 
                Files:
                    entity.py           |       The base entity file.
                    player.py           |       Traits unique to the player (i.e. controllable via keyboard).
                    stage.py            |       Traits unique to static parts of the map.

            Files:
                constants.py            |       Constant variables that don't change while the program is running.
                settings.py             |       Settings unique to each device: player preferences, etc.

        /maps
            Contains the map files, to be loaded by the part of the engine that loads maps.

        /resources
            Image, sound, and music files. Anything else that isn't a map or code.

    Game imports: If you create a new .py file, you may need to import it here!
    Example:
        from game.engine.physics import Physics
    This would import the `Physics` class from the `physics.py` file in /game/engine
"""
import arcade
import os
import json
import random

from game import constants
from game.engine.arcade_engine import ArcadeEngine
from game.entity.player import Player
from game.entity.stage import Stage

if not os.path.exists(constants.SETTINGS_FILE):
    print("Settings file not detected, creating default.")
    default_settings_file = open(constants.SETTINGS_FILE, "x")
    default_settings_file.write(constants.DEFAULT_SETTINGS)
    default_settings_file.close()
file = open(constants.SETTINGS_FILE)
SETTINGS = json.load(file)

def main():
    entities = arcade.Scene()
    """ 
        Entity Types:
            Player: Entity with separate stats and user-control
            Projectiles: Moving object, probably disappears after colliding with something.
            Stage: Populated by the map loader, includes walls, floors, and ceilings.
            Trigger: Invisible entities that activate code when touched by specified entities.
            Enemy: Entity with movement capabilities and other AI.
            Drop: Item that can be picked up by the player.
    """
    # Add initial entities here:
    entities = populate(entities)
    engine = ArcadeEngine(
         entities, 
         constants.WINDOW_TITLE, 
         SETTINGS["monitor"], 
         SETTINGS["fullscreen"], 
         SETTINGS["windowed_width"], 
         SETTINGS["windowed_height"]
    )
    engine.setup()
    engine.run()

def populate(entities=arcade.Scene()):
    # entities.add_sprite("player", arcade.Sprite(constants.PLAYER_IMAGES[0], center_x=500, center_y=500))
    entities.add_sprite("player", Player(constants.PLAYER_IMAGES, constants.PLAYER_CONTROLS))
    entities.get_sprite_list("player").sprite_list[0].teleport(500, 500)
    # entities.add_sprite("stage", arcade.Sprite("res/stage/platform1.png", center_x=500, center_y=100))
    entities.add_sprite_list("stage", use_spatial_hash=True)
    # entities.add_sprite("stage", Stage("res/stage/platform1.png", 500, 100))
    # creates floor for total length with randomized images
    for x in range(0, 12500, 100):
            floor = arcade.Sprite(constants.FLOOR_IMAGES[random.randint(0,3)])
            floor.center_x = x
            floor.center_y = constants.FLOOR_HEIGHT

            entities.add_sprite("stage", floor)
    # adds a (4 pngs) platform at the first height so other heights can be reached 
    for x in range(800, 1056, 100):
        platform = arcade.Sprite(constants.FLOOR_IMAGES[random.randint(0,3)])
        platform.center_x = x
        platform.center_y = constants.PLATFORM_HEIGHTS[0]
        entities.add_sprite("stage", platform)

    # continues randomized platforms at random (given) platform heights for rest of the map
    for x in range(1184, 12500, 100):
        platformChance = random.randint(0,4)
        gemChance = random.randint(0, 5)
        # if 4 is the random int, it will leave a blank space instead of a platform
        if platformChance == 4:
             continue

        platform = arcade.Sprite(constants.FLOOR_IMAGES[platformChance])
        platform.center_x = x
        platform.center_y = constants.PLATFORM_HEIGHTS[random.randint(0,2)] #gives height of platform from list in Constants
        entities.add_sprite("stage", platform)

        #when gemChance == 5, we create a gem in that spot
        if gemChance == 5:
            bufferHeight = 80
            gem = arcade.Sprite(constants.GEM_IMAGES[random.randint(0, len(constants.GEM_IMAGES) - 1)])
            gem.center_x = x
            gem.center_y = platform.center_y + bufferHeight
            entities.add_sprite("drops", gem)
        
    return entities

if __name__ == "__main__":
    main()