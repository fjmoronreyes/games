from sprite import Sprite
import random


class Particle(Sprite):
    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000, -1000)  # Initial off-screen position
        self.frame = 0

    def explode(self, start_x, start_y):
        self.goto(start_x, start_y)
        self.setheading(random.randint(0, 360))
        self.frame = 1

    def move(self):
        if self.frame > 0 and self.frame <= 20:
            self.fd(10)
            self.frame += 1
        if self.frame > 20:
            self.frame = 0
            self.goto(-1000, -1000)
