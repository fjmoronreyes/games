import random
from sprite import Sprite


class Enemy(Sprite):
    """
    Represents an enemy in the game, inheriting from Sprite.
    Enemies move randomly within the game boundaries and have specific interactions with other game entities.

    Attributes:
        speed (int): Speed at which the enemy moves.
    """

    def __init__(
        self,
        sprite_shape: str = "circle",
        color: str = "red",
        start_x: int = -100,
        start_y: int = 0,
    ):
        """
        Initialize a new enemy.

        Args:
            sprite_shape (str): The shape of the enemy, defaults to 'circle'.
            color (str): The color of the enemy, defaults to 'red'.
            start_x (int): The starting x-coordinate of the enemy, defaults to -100.
            start_y (int): The starting y-coordinate of the enemy, defaults to 0.
        """
        super().__init__(sprite_shape, color, start_x, start_y)
        self.speed = 6
        self.setheading(random.randint(0, 360))

    def move(self) -> None:
        """
        Move the enemy forward continuously while checking and responding to boundary limits.
        """
        self.fd(self.speed)
        self.check_and_handle_boundaries()

    def check_and_handle_boundaries(self) -> None:
        """
        Check if the enemy has reached the boundaries of the game area and adjust position and heading.
        """
        if self.xcor() > 290:
            self.setx(290)
            self.rt(
                60
            )  # Random turn direction, possibly make consistent across entities
        elif self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        elif self.ycor() < -290:
            self.sety(-290)
            self.rt(60)
