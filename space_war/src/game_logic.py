import turtle


class Game:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.ht()

    def draw_border(self):
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()

    def show_status(self):
        self.pen.undo()
        msg = f"Score: {self.score}  Lives: {self.lives}"
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))

    def update_score(self, points):
        self.score += points
        self.show_status()

    def update_lives(self, delta):
        self.lives += delta
        self.show_status()

    def reset_game(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.show_status()

    def game_over(self):
        self.state = "game_over"
        self.pen.goto(-150, 0)
        self.pen.write("GAME OVER", font=("Arial", 30, "bold"))
