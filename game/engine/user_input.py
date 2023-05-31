class UserInput():
    def __init__(self):
        self._key_list = [] # List of keys currently pressed
        self._mouse_list = [] # List of active mouse actions

    def key_down(self, key):
        self._key_list.append(key)

    def key_up(self, key):
        self._key_list.remove(key)

    def mouse_down(self, button):
        self._mouse_list.append(button)

    def mouse_up(self, button):
        self._mouse_list.remove(button)

    def get_direction(self, up, down, right, left, magnitude=1):
        x, y = 0, 0
        # for key in self._key_list:
        if up in self._key_list:
            y = 1 * magnitude
        elif down in self._key_list:
            y = -1 * magnitude
        if right in self._key_list:
            x = 1 * magnitude
        elif left in self._key_list:
            x = -1 * magnitude
        return (x, y)