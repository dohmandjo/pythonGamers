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

    def get_direction(self, ups, downs, rights, lefts, magnitude=1):
        x, y = 0, 0
        for key in ups:
            if key in self._key_list:
                y = 1 * magnitude
    # don't need movement for downward right now
        # for key in downs:
        #     if key in self._key_list:
        #         y = -1 * magnitude
        for key in rights:
            if key in self._key_list:
                x = 1 * magnitude
        for key in lefts:
            if key in self._key_list:
                x = -1 * magnitude
        return (x, y)
        
        # FOR ONLY ONE BUTTON PER KEY MAPPING
        # for key in self._key_list:
        if ups in self._key_list:
            y = 1 * magnitude
        elif downs in self._key_list:
            y = -1 * magnitude
        if rights in self._key_list:
            x = 1 * magnitude
        elif lefts in self._key_list:
            x = -1 * magnitude
        return (x, y)