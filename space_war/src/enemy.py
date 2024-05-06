import random
from sprite import Sprite


class Enemy(Sprite):
    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.speed = 6
        self.setheading(random.randint(0, 360))
