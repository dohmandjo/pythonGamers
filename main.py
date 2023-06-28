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

from game import constants
from game.engine.arcade_engine import ArcadeEngine
from game.entity.player import Player
from game.entity.stage import Stage

if os.path.exists(constants.SETTINGS_FILE):
    file = open(constants.SETTINGS_FILE)
    SETTINGS = json.load(file)
else:
    print("Settings file not detected, creating default.")
    default_settings_file = open(constants.SETTINGS_FILE, "x")
    default_settings_file.write(constants.DEFAULT_SETTINGS)
    default_settings_file.close()
    SETTINGS = json.load(constants.DEFAULT_SETTINGS)

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
    # TEST PLATFORM
    for x in range(0, 1250, 64):
            floor = Stage("res/stage/platform1.png", x, 64)
            entities.add_sprite("stage", floor)
    return entities

if __name__ == "__main__":
    main()