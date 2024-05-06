from sprite import Sprite
import random


class Ally(Sprite):
    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.speed = 8
        self.setheading(random.randint(0, 360))

    def move(self):
        """
        Move the sprites forward
        """
        self.fd(self.speed)

        # Boundary detection

        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)
