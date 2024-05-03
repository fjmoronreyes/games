import os
import turtle
import random

turtle.fd(0)  # required by MacOS to show the window
turtle.speed(0)  # control the speed of the animation
turtle.bgcolor("black")  # background color
turtle.ht()  # hide the default turtle
turtle.setundobuffer(1)  # saves memory
turtle.tracer(1)  # speeds up drawing


class Sprite(turtle.Turtle):
    def __init__(self, sprite_shape, color, start_x, start_y):
        turtle.Turtle.__init__(self, shape=sprite_shape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(start_x, start_y)
        self.speed = 1


# Instantiate
sprite_shape = "triangle"
color = "white"
start_x = 0
start_y = 0

player = Sprite(
    sprite_shape=sprite_shape, color=color, start_x=start_x, start_y=start_y
)

delay = input("Press enter to finish. --")
