from sprite import Sprite
import os


class Missile(Sprite):
    def __init__(self, sprite_shape, color, start_x, start_y):
        super().__init__(sprite_shape, color, start_x, start_y)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.movement_speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)  # Initial off-screen position

    def fire(self, x, y, heading):
        if self.status == "ready":
            # Play missile sound (ATM only for macOS)
            os.system("afplay ../media/laser.mp3&")
            self.goto(x, y)
            self.setheading(heading)
            self.status = "firing"

    def move(self):
        if self.status == "ready":
            self.goto(-1000, 1000)

        if self.status == "firing":
            self.fd(self.movement_speed)

        # Border check
        if (
            self.xcor() < -290
            or self.xcor() > 290
            or self.ycor() < -290
            or self.ycor() > 290
        ):
            self.goto(-1000, 1000)
            self.status = "ready"
