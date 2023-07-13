from game.entity.entity import Entity
from game.engine.user_input import UserInput

class Player(Entity):

    def __init__(self, sprite_sheet, controls):
        self.controls = controls
        self.acceleration_speed = 1
        self.top_speed = 20
        self.jump_height = 20
        self.can_jump = False
        self.air_strafe = True
        self.has_jumped = False
        super().__init__(sprite_sheet)

    def handle_user_input(self, input_service:UserInput):
        ups = self.controls[0]
        downs = self.controls[1]
        rights = self.controls[2]
        lefts = self.controls[3]
        new_acceleration = input_service.get_direction(ups, downs, rights, lefts, self.acceleration_speed)

        if self.air_strafe or self.can_jump:
            if new_acceleration[0] != 0:
                self.change_x = self.top_speed_limiter(self.change_x + new_acceleration[0], self.top_speed)
            elif (self.change_x > 0):
                if self.change_x > self.acceleration_speed:
                    self.change_x -= self.acceleration_speed
                else:
                    self.change_x = 0
            elif (self.change_x < 0):
                if abs(self.change_x) > self.acceleration_speed:
                    self.change_x += self.acceleration_speed
                else:
                    self.change_x = 0

        if (new_acceleration[1] != 0) and self.can_jump:
            self.change_y += self.jump_height
            self.has_jumped = True

    def top_speed_limiter(self, speed, limit):
        return min(max(speed, -1 * limit), limit)