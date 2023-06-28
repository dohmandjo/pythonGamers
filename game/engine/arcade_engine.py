import arcade
from game.engine.user_input import UserInput
from game.engine.physics import Physics

class ArcadeEngine(arcade.Window):
    """ 
        ArcadeEngine handles the brunt of interactions with the Arcade engine.
        Various evens are called below, and given handles that send them off to other
        places around the file structure. They *should* be pretty self-explanatory.
    """
    def __init__(self, entities:arcade.Scene, window_title, target_display, fullscreen, width, height):
        self.entities = entities
        window_size = arcade.get_display_size(target_display)
        self.player1 = self.entities["player"][0]
        super().__init__(width, height, window_title)
        if fullscreen == "True":
            super().set_fullscreen(True, arcade.get_screens()[target_display], None, window_size[0], window_size[1])
        self.layers = {}
        self.backgrounds = arcade.SpriteList()
        self.physics = Physics(self.entities)
        self.user_input = UserInput()

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.layers["background"] = arcade.Camera(self.width, self.height)
        self.layers["level"] = arcade.Camera(self.width, self.height)
        self.layers["gui"] = arcade.Camera(self.width, self.height)
        self.x_limit = max([sprite.center_x for sprite in self.entities.get_sprite_list("stage")])
        print(self.x_limit)
        for i in range(1, 7):
            self.backgrounds.append(arcade.Sprite(f"res/background/bg-layer{i}.png"))

    def on_update(self, delta_time: float):
        """
            This function is where game 'ticks' are processed. Any code that you
            want to run on every frame, so to speak, must be executed from here.
        """
        for player in self.entities["player"]:
            player.handle_user_input(self.user_input)
        self.physics.tick()
        self.camera_update()
        x = self.layers["background"].viewport_width / 2
        y = self.layers["background"].viewport_height / 2
        for i, layer in enumerate(self.backgrounds):
            if i == 0:
                layer.center_x = x
            else:
                layer.center_x = x + ((self.x_limit / 2 - self.player1.center_x) / (i * 3))
            layer.center_y = y
        return super().on_update(delta_time)
    
    def on_draw(self):
        """
            This function is where game objects are drawn.
        """
        self.clear()
        self.layers["background"].use()
        self.backgrounds.draw()
        self.layers["level"].use()
        self.entities.draw()
        self.layers["gui"].use()
        # Draw GUI elements here!!

        return super().on_draw()
    
    def camera_update(self):
        screen_center_x = self.player1.center_x - (self.layers["level"].viewport_width  / 2)
        screen_center_y = self.player1.center_y - (self.layers["level"].viewport_height / 2)

        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.layers["level"].move_to(player_centered)
    
    def on_key_press(self, symbol: int, modifiers: int):
        """
            A class should be instantiated to handle the user input.
            Call to that class here. This function executes when a key is pressed DOWN.
        """
        self.user_input.key_down(symbol)
        return super().on_key_press(symbol, modifiers)
    
    def on_key_release(self, symbol: int, modifiers: int):
        """
            A class should be instantiated to handle the user input.
            Call to that class here. This function executes when a key is pressed UP.
        """
        self.user_input.key_up(symbol)
        return super().on_key_release(symbol, modifiers)
    
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """
            A class should be instantiated to handle the user input.
            Call to that class here. This function executes a mouse button is clicked DOWN.
        """
        return super().on_mouse_press(x, y, button, modifiers)
    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        """
            A class should be instantiated to handle the user input.
            Call to that class here. This function executes a mouse button is clicked UP.
        """
        return super().on_mouse_release(x, y, button, modifiers)
    
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        """
            A class should be instantiated to handle the user input.
            Call to that class here. This function executes when the mouse moves.
        """
        return super().on_mouse_motion(x, y, dx, dy)