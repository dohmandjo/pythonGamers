from game.entity.entity import Entity

class Stage(Entity):

    def __init__(self, sprite, x, y):
        super().__init__([sprite], x, y)