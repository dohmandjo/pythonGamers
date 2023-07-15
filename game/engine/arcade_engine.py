import arcade
from game.engine.user_input import UserInput
from game.engine.physics import Physics
import time
from game import constants

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
        self.score = len(self.entities["drops"])
        # Add sounds
        self.bgm = arcade.load_sound("res/sfx/background.wav")
        self.coalsfx = arcade.load_sound("res/sfx/coal.wav")
        self.gemsfx = arcade.load_sound("res/sfx/gemget.wav")
        self.startsfx = arcade.load_sound("res/sfx/start.wav")
        self.winsfx = arcade.load_sound("res/sfx/win.wav")
        #arcade.Sound(self.bgm, streaming=True)
        self.music_list = []
        self.current_song_index = 0
        self.music = None

    def play_song(self):
        """ Play the song. """
        # Play the next song
        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(constants.MUSIC_VOLUME)
        # This is a quick delay. If we don't do this, our elapsed time is 0.0
        # and on_update will think the music is over and advance us to the next
        # song before starting this one.
        time.sleep(0.03)
     
    def advance_song(self):
         """ Advance our pointer to the next song. This does NOT start the song. """
         if self.current_song_index == 0:
             self.current_song_index = 1
        #Switch to final song after game completion
         if self.player1.can_move == False:
            self.current_song_index = 2

    def setup(self):
       
        arcade.set_background_color(arcade.color.BLACK)
        self.layers["background"] = arcade.Camera(self.width, self.height)
        self.layers["level"] = arcade.Camera(self.width, self.height)
        self.layers["gui"] = arcade.Camera(self.width, self.height)
        self.x_limit = max([sprite.center_x + (sprite.width / 2) for sprite in self.entities.get_sprite_list("stage")])
        self.player1.teleport(self.x_limit / 2, self.player1.center_y)
        for i in range(1, 8):
            self.backgrounds.append(arcade.Sprite(f"res/background/bg-layer{i}.png", scale=1.5))
        # List of music
        self.music_list = ["res/sfx/start.wav","res/sfx/background.wav","res/sfx/end.wav"]
        self.play_song()
        self.score = len(self.entities["drops"])

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
            # if i == 0:
            #     layer.center_x = x
            # else:
            layer.center_x = x + (self.x_limit / 2 - self.layers["level"].position.x) / ((9 - i) * 3)
            layer.center_y = y
        # Add to gem pickup and coal pickup
        gemget = arcade.check_for_collision_with_list(self.entities["player"][0], self.entities["drops"])
        for gem in gemget:
           gem.remove_from_sprite_lists()
           arcade.play_sound(self.gemsfx)
           self.score = len(self.entities["drops"])
           if len(self.entities["drops"]) == 0 :
               self.player1.can_move = False
               self.physics.gravity_constant = 0
               # Victory SFX
               arcade.play_sound(self.winsfx,3)
               
        # arcade.play_sound(coalsfx,1.0,-1,False,1)
       
        position = self.music.get_stream_position(self.current_player)
 
        # The position pointer is reset to 0 right after we finish the song.
        # This makes it very difficult to figure out if we just started playing
        # or if we are doing playing.
        if position == 0.0:
             self.advance_song()
             self.play_song()
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
        score_text = f"Items Left: {self.score}"
        arcade.draw_text(score_text, constants.SCORE_DISPLAY , constants.SCORE_DISPLAY, arcade.csscolor.WHITE, 18)

        return super().on_draw()
    
    def camera_update(self):
        screen_center_x = self.player1.center_x - (self.layers["level"].viewport_width  / 2)
        screen_center_y = self.player1.center_y - (self.layers["level"].viewport_height / 2)
        

        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        # Don't let camera travel past map limit
        if screen_center_x > self.x_limit - (self.layers["level"].viewport_width):
            screen_center_x = self.x_limit - (self.layers["level"].viewport_width)
        if screen_center_y > self.x_limit - (self.layers["level"].viewport_width):
            screen_center_y = self.x_limit - (self.layers["level"].viewport_width)
        player_centered = screen_center_x, screen_center_y * .75

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
