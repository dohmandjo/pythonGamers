class Physics():
    def __init__(self):
        pass

    def tick(self, entities):
        for player in entities["player"]:
            self.move(player, player.top_speed)

    def detect_collision(self, entity1, entity2):
        pass

    def move(self, entity, limit=-1):
        pos_x = entity.center_x + self.cap(entity.velocity[0] + entity.acceleration[0], limit)
        pos_y = entity.center_y + self.cap(entity.velocity[1] + entity.acceleration[1], limit)
        entity.center_x = pos_x
        entity.center_y = pos_y

    def cap(self, value, cap):
        """ 
            Limits the value given by the value 'cap', positive or negative.
            Since cap should be a scalar value, any negative value will return unchanged.
        """
        if cap <= 0:
            return value
        neg_cap = cap * -1
        return max(neg_cap, min(value, cap))