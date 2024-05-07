import turtle
from typing import NoReturn


class Sprite(turtle.Turtle):
    """
    Base class for all movable objects in the game, providing fundamental attributes and methods like movement and collision detection.
    Inherits from turtle.Turtle to utilize Turtle graphics functionalities.
    """

    def __init__(
        self, sprite_shape: str, color: str, start_x: int, start_y: int
    ) -> NoReturn:
        """
        Initializes a new sprite object with a specified shape, color, and initial position.

        Args:
            sprite_shape (str): The shape of the sprite, which can be any shape registered in the Turtle graphics system.
            color (str): The color of the sprite.
            start_x (int): The initial x-coordinate of the sprite.
            start_y (int): The initial y-coordinate of the sprite.
        """
        super().__init__(shape=sprite_shape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(start_x, start_y)
        self.speed = 1

    def move(self) -> NoReturn:
        """
        Moves the sprite forward by its movement speed. Checks and handles boundaries of the game area.
        """
        self.fd(self.speed)

        # Boundary detection

        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_collision(self, other) -> bool:
        """
        Determines if this sprite has collided with another sprite based on their positions.

        Args:
            other (Sprite): Another sprite object to check for collision.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        if (
            (self.xcor() >= (other.xcor() - 20))
            and (self.xcor() <= (other.xcor() + 20))
            and (self.ycor() >= (other.ycor() - 20))
            and (self.ycor() <= (other.ycor() + 20))
        ):
            return True
        return False
