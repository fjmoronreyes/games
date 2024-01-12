import turtle


class Paddle(turtle.Turtle):
    def __init__(self, color, shape, x, y):
        super().__init__()
        self.speed(0)
        self.shape(shape)
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
