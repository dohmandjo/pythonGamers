import arcade
from game import constants

""" 
    This is the basic entity template. For the most part, every entity should 
    at least have a sprite to associate it with and a starting position.

    Other data that will be used by *all* other entities should be added here.
    If it's specific to a type of entity (player, pickups, etc.) it should go
    in its specific class.
"""

class Entity(arcade.Sprite):

    def __init__(self, sprite_sheet=[None], x=0, y=0):
        """ 
            Initialize the arcade.Sprite class. 
            The bare minimum `Sprite` requires is an image to point to, which *can* be `None`.
            Other things you can implement here are scaling and flipping the image.
        """
        super().__init__(sprite_sheet[0], center_x=x, center_y=y)
    
    def teleport(self, x, y):
        self.center_x = x
        self.center_y = y