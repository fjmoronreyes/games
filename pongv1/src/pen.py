import turtle


class Pen(turtle.Turtle):
    def __init__(self, score_a, score_b):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scores(score_a, score_b)

    def update_scores(self, score_a, score_b):
        self.clear()
        self.write(
            f"Player 1: {score_a} | Player 2: {score_b}",
            align="center",
            font=("Courier", 24, "normal"),
        )
