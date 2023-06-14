import arcade

class Physics(arcade.PhysicsEnginePlatformer):
    def __init__(self, entities: arcade.Scene):
        self.player = entities.get_sprite_list("player").sprite_list[0]
        # player_sprite = player
        gravity = 1
        walls = entities.get_sprite_list("stage")
        super().__init__(self.player, gravity_constant=gravity, walls=walls)

    def tick(self):
        super().update()
        self.player.can_jump = self.can_jump()