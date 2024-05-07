import os
from sprite import Sprite
from typing import NoReturn


class Missile(Sprite):
    """
    Represents a missile object in the game, inheriting from Sprite.
    The missile has specific attributes for its firing status and movement speed.
    """

    def __init__(
        self,
        sprite_shape: str = "triangle",
        color: str = "yellow",
        start_x: int = 0,
        start_y: int = 0,
    ):
        """
        Initialize a new missile with default values for shape, color, and initial position.

        Args:
            sprite_shape (str): The geometric shape of the missile.
            color (str): The color of the missile.
            start_x (int): Initial x-coordinate of the missile.
            start_y (int): Initial y-coordinate of the missile.
        """
        super().__init__(sprite_shape, color, start_x, start_y)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.movement_speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)  # Initial off-screen position

    def fire(self, x: int, y: int, heading: int) -> NoReturn:
        """
        Fires the missile if it is ready, setting its position, direction, and changing its status to 'firing'.

        Args:
            x (int): The x-coordinate from which to fire the missile.
            y (int): The y-coordinate from which to fire the missile.
            heading (int): The heading angle for the missile to move towards.
        """
        if self.status == "ready":
            # Play missile sound (ATM only for macOS)
            os.system("afplay ../media/laser.mp3&")
            self.goto(x, y)
            self.setheading(heading)
            self.status = "firing"

    def move(self) -> NoReturn:
        """
        Moves the missile based on its current status. If the missile is 'firing', it advances forward.
        Also checks and handles if the missile reaches the boundaries of the play area.
        """
        if self.status == "ready":
            self.goto(-1000, 1000)

        if self.status == "firing":
            self.fd(self.movement_speed)

        self.check_and_handle_boundaries()

    def check_and_handle_boundaries(self) -> NoReturn:
        """
        Checks if the missile has reached the boundaries of the game area and resets if it does.
        """
        if (
            self.xcor() < -290
            or self.xcor() > 290
            or self.ycor() < -290
            or self.ycor() > 290
        ):
            self.goto(-1000, 1000)
            self.status = "ready"
