import arcade

class ArcadeEngine(arcade.Window):
    def __init__(self, entities, window_title, target_display, fullscreen, width, height):
        window_size = arcade.get_display_size(target_display)
        super().__init__(width, height, window_title)
        if fullscreen:
            super().set_fullscreen(True, arcade.get_screens()[target_display], None, window_size[0], window_size[1])

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, delta_time: float):
        """
            This function is where game 'ticks' are processed. Any code that you
            want to run on every frame, so to speak, must be executed from here.
        """
        return super().on_update(delta_time)
    
    def on_draw(self):
        """
            This function is where game objects are drawn.
        """
        return super().on_draw()
    
    def on_key_press(self, symbol: int, modifiers: int):
        """
            A class should be instantiated to handle the user input.
            Call to that class here. This function executes when a key is pressed DOWN.
        """
        return super().on_key_press(symbol, modifiers)
    
    def on_key_release(self, symbol: int, modifiers: int):
        """
            A class should be instantiated to handle the user input.
            Call to that class here. This function executes when a key is pressed UP.
        """
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