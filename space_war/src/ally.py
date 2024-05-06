from sprite import Sprite
import random


class Ally(Sprite):
    """
    Represents an ally in the game, inheriting from Sprite.
    Allies move randomly within the game boundaries and respond to interactions.

    Attributes:
        speed (int): Speed at which the ally moves.
    """

    def __init__(
        self,
        sprite_shape: str = "square",
        color: str = "blue",
        start_x: int = 100,
        start_y: int = 0,
    ):
        """
        Initialize a new ally.

        Args:
            sprite_shape (str): The shape of the ally, default to 'square'.
            color (str): The color of the ally, default to 'blue'.
            start_x (int): The starting x-coordinate of the ally, default to 100.
            start_y (int): The starting y-coordinate of the ally, default to 0.
        """
        super().__init__(sprite_shape, color, start_x, start_y)
        self.speed = 8
        self.setheading(random.randint(0, 360))

    def move(self) -> None:
        """
        Move the ally forward continuously while checking and responding to boundary limits.
        """
        self.fd(self.speed)
        self.check_and_handle_boundaries()

    def check_and_handle_boundaries(self) -> None:
        """
        Check if the ally has reached the boundaries of the game area and adjust position and heading.
        """
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
        elif self.xcor() < -290:
            self.setx(-290)
            self.lt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)
        elif self.ycor() < -290:
            self.sety(-290)
            self.lt(60)
