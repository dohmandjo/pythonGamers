from game.entity.entity import Entity

class Player(Entity):

    def __init__(self, image_file, controls, top_speed, acceleration):
        self.base_image = image_file[0]
        self.run_image = image_file[1]
        super().__init__(self.base_image)
        self.controls = controls
        self.top_speed = top_speed
        self.top_acceleration = acceleration
        print(f"Creating player with the following controls: \n\tUP: {self.controls[0]} \n\tDown: {self.controls[1]} \n\tRight: {self.controls[2]} \n\tLeft: {self.controls[3]}")

    def handle_user_input(self, input_service):
        up = self.controls[0]
        down = self.controls[1]
        right = self.controls[2]
        left = self.controls[3]
        new_acceleration = input_service.get_direction(up, down, right, left, self.top_acceleration)

        if new_acceleration[0] != 0:
            self.acceleration = (new_acceleration[0], self.acceleration[1])
        elif self.velocity[0] > 0:
            if self.top_acceleration > self.velocity[0]:
                self.acceleration = (self.velocity[0] * -1, self.acceleration[1])
            else:
                self.acceleration = (self.top_acceleration * -1, self.acceleration[1])
        elif self.velocity[0] < 0:
            if self.top_acceleration > self.velocity[0] * -1:
                self.acceleration = (self.velocity[0] * -1, self.acceleration[1]) 
            else:
                self.acceleration = (self.top_acceleration, self.acceleration[1])
        elif self.velocity[0] == 0:
            self.acceleration = (0, self.acceleration[1])