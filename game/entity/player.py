from game.entity.entity import Entity

class Player(Entity):

    def __init__(self, image_file):
        super().__init__(image_file)