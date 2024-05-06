import turtle
import os
import random


def play_sound(sound_path):
    os.system(f"afplay {sound_path}&")


def manage_collision(entity, sound="../media/explosion.mp3"):
    play_sound(sound)
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    entity.goto(x, y)
