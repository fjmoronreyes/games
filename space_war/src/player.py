from sprite import Sprite


class Player(Sprite):
    """
    Represents the player's character in the game, inheriting from Sprite.
    The player can move around, accelerate, and decelerate within the game space.

    Attributes:
        speed (int): The current speed of the player.
        lives (int): The number of lives the player has remaining.
    """

    def __init__(
        self,
        sprite_shape: str = "triangle",
        color: str = "white",
        start_x: int = 0,
        start_y: int = 0,
    ):
        """
        Initializes a new player with specific attributes.

        Args:
            sprite_shape (str): The shape of the player, default is 'triangle'.
            color (str): The color of the player, default is 'white'.
            start_x (int): The starting x-coordinate of the player.
            start_y (int): The starting y-coordinate of the player.
        """
        super().__init__(sprite_shape, color, start_x, start_y)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        """
        Rotates the player 45 degrees to the left.
        """
        self.lt(45)

    def turn_right(self):
        """
        Rotates the player 45 degrees to the right.
        """
        self.rt(45)

    def accelerate(self):
        """
        Increases the player's speed by 1 unit.
        """
        self.speed += 1

    def decelerate(self):
        """
        Decreases the player's speed by 1 unit.
        """
        self.speed -= 1
