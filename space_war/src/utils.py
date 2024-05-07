import os
from typing import Any, NoReturn
import random


def play_sound(sound_path: str) -> NoReturn:
    """
    Plays a sound from a given file path using a system call.

    Args:
        sound_path (str): The file path to the sound file to be played.
    """
    # Check if the platform is macOS, use 'afplay'; adapt for other platforms if necessary
    if os.name == "posix":
        os.system(f"afplay {sound_path}&")
    else:
        print("Sound playing not supported on this operating system.")


def manage_collision(
    entity: Any, sound_path: str = "../media/explosion.mp3"
) -> NoReturn:
    """
    Handles the actions to be taken when a collision occurs, including playing a sound
    and relocating the entity to a random position within the game boundaries.

    Args:
        entity (Any): The game entity that has collided. It must have a 'goto' method.
        sound_path (str): The file path to the explosion sound file.
    """
    play_sound(sound_path)
    # Randomly place the entity within a defined range
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    entity.goto(x, y)
