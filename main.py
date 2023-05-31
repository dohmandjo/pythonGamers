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
# import sys
os.chdir(os.getcwd())

from game import constants
try: 
    from game import settings
except ImportError:
    print("`settings.py` was not found. Creating one with the default values.")
    settings = open("game/settings.py", "x")
    settings.write(constants.DEFAULT_SETTINGS)
    settings.close()
    exit()

# from game.engine import physics
from game.engine.arcade_engine import ArcadeEngine
from game.entity.player import Player


def main():
    entities = {}
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


    INPUT_SERVICE = None # ArcadeInputService()
    OUTPUT_SERVICE = None # ArcadeOutputService()

    engine = ArcadeEngine(entities, constants.WINDOW_TITLE, settings.monitor, settings.fullscreen, settings.windowed_width, settings.windowed_height)

    arcade.run()

def populate(entities):
    entities["player"] = [Player(constants.PLAYER_IMAGES, constants.PLAYER_CONTROLS, constants.PLAYER_SPEED, constants.PLAYER_ACCEL)]
    return entities

if __name__ == "__main__":
    # if os.path.isfile("game/settings.py"):
    #     from game.settings import *
    # else:
    #     settings = open("game/settings.py", "a")
    #     settings.write(constants.DEFAULT_SETTINGS)
    #     settings.close()
    #     from game.settings import *
    main()