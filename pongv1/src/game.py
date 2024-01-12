import os
import turtle

from ball import Ball
from paddle import Paddle
from pen import Pen


class Game:
    def __init__(self):
        turtle.colormode(255)
        self.window = turtle.Screen()
        self.window.title("Pong beginner V1")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        self.score_a = 0
        self.score_b = 0

        self.paddle_a = Paddle("white", "square", -350, 0)
        self.paddle_b = Paddle("white", "square", 350, 0)
        self.ball = Ball(color="white", shape="square", x=0, y=0, dx=3, dy=-1)
        self.pen = Pen(self.score_a, self.score_b)

        self.window.listen()
        self.window.onkeypress(self.paddle_a.move_up, "w")
        self.window.onkeypress(self.paddle_a.move_down, "s")
        self.window.onkeypress(self.paddle_b.move_up, "Up")
        self.window.onkeypress(self.paddle_b.move_down, "Down")

    def update_scores(self):
        self.pen.clear()
        self.pen.write(
            f"Player 1: {self.score_a} | Player 2: {self.score_b}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    def play_sound(self):
        os.system("afplay bounce_sound.wav&")

    def run(self):
        # Main game loop
        while True:
            self.window.update()

            # Move the ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # Border checking
            if self.ball.ycor() > 290 or self.ball.ycor() < -290:
                self.ball.dy *= -1
                self.play_sound()

            # Check for scoring
            if self.ball.xcor() > 390 or self.ball.xcor() < -390:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                if self.ball.xcor() > 0:
                    self.score_a += 1
                else:
                    self.score_b += 1
                self.update_scores()

            if (
                self.paddle_b.xcor() - 10 < self.ball.xcor() < self.paddle_b.xcor() + 10
                and self.paddle_b.ycor() + 50
                > self.ball.ycor()
                > self.paddle_b.ycor() - 40
            ):
                self.ball.setx(self.paddle_b.xcor() - 10)
                self.ball.dx *= -1
                self.play_sound()

            if (
                self.paddle_a.xcor() + 10 > self.ball.xcor() > self.paddle_a.xcor() - 10
                and self.paddle_a.ycor() + 50
                > self.ball.ycor()
                > self.paddle_a.ycor() - 40
            ):
                self.ball.setx(self.paddle_a.xcor() + 10)
                self.ball.dx *= -1
                self.play_sound()


if __name__ == "__main__":
    game = Game()
    game.run()
