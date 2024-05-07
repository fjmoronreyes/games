import turtle


class Game:
    """
    Manages the state and visual representation of the game including score, levels, and lives.
    """

    def __init__(self):
        """
        Initializes the game with default settings.
        """
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.lives = 3
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.ht()

    def draw_border(self) -> None:
        """
        Draws a border around the playable area of the game.
        """
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()

    def show_status(self) -> None:
        """
        Updates the game's status display, showing the current score and remaining lives.
        """
        self.pen.undo()
        msg = f"Score: {self.score}  Lives: {self.lives}"
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))

    def update_score(self, points: int) -> None:
        """
        Updates the game's score and refreshes the status display.

        Args:
            points (int): The amount to add to the current score.
        """
        self.score += points
        self.show_status()

    def update_lives(self, delta: int) -> None:
        """
        Updates the number of lives remaining and refreshes the status display.

        Args:
            delta (int): The number to add to the current lives (can be negative).
        """
        self.lives += delta
        self.show_status()

    def reset_game(self) -> None:
        """
        Resets the game to its initial state, including score, lives, and level.
        """
        self.score = 0
        self.lives = 3
        self.level = 1
        self.show_status()

    def game_over(self) -> None:
        """
        Ends the game and displays a 'GAME OVER' message.
        """
        self.state = "game_over"
        self.pen.goto(-150, 0)
        self.pen.write("GAME OVER", font=("Arial", 30, "bold"))
