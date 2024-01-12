import turtle


class Ball(turtle.Turtle):
    def __init__(self, color, shape, x, y, dx, dy):
        super().__init__()
        self.speed(0)
        self.shape(shape)
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.dx = dx
        self.dy = dy
