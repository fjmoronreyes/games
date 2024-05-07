import random
from sprite import Sprite
from typing import NoReturn


class Particle(Sprite):
    """
    Represents a particle effect in the game, inheriting from Sprite.
    Particles are used for visual effects, like explosions.

    Attributes:
        frame (int): The current frame of the particle's animation lifecycle.
    """

    def __init__(
        self,
        sprite_shape: str = "circle",
        color: str = "orange",
        start_x: int = 0,
        start_y: int = 0,
    ):
        """
        Initialize a new particle with default values for shape, color, and initial position.

        Args:
            sprite_shape (str): The geometric shape of the particle.
            color (str): The color of the particle.
            start_x (int): Initial x-coordinate of the particle.
            start_y (int): Initial y-coordinate of the particle.
        """
        super().__init__(sprite_shape, color, start_x, start_y)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000, -1000)  # Start off-screen
        self.frame = 0

    def explode(self, start_x: int, start_y: int) -> NoReturn:
        """
        Trigger the particle's explosion effect from a specific location.

        Args:
            start_x (int): The x-coordinate where the explosion starts.
            start_y (int): The y-coordinate where the explosion starts.
        """
        self.goto(start_x, start_y)
        self.setheading(random.randint(0, 360))
        self.frame = 1

    def move(self) -> NoReturn:
        """
        Handle the movement and lifecycle of the particle.
        The particle moves forward if it is active and resets after completing its lifecycle.
        """
        if 0 < self.frame <= 20:
            self.fd(10)
            self.frame += 1
        elif self.frame > 20:
            self.reset_particle()

    def reset_particle(self) -> NoReturn:
        """
        Resets the particle to an inactive state and moves it off-screen.
        """
        self.frame = 0
        self.goto(-1000, -1000)
