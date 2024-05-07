import turtle
from player import Player
from missile import Missile


def update_screen() -> None:
    """
    Refresh the turtle graphics screen to reflect any changes made.
    """
    turtle.update()


def setup_screen() -> None:
    """
    Configure the initial settings of the turtle screen to prepare the game window.
    This includes setting the background, window size, title, and other turtle-specific configurations.
    """
    turtle.fd(0)  # Required by MacOS to show the window
    turtle.speed(0)  # Set the animation speed to the fastest
    turtle.bgcolor("black")  # Set the background color of the game screen
    turtle.bgpic("../media/starfield.gif")  # Set the background image
    turtle.title("SpaceWar!")  # Set the window title
    turtle.ht()  # Hide the default turtle graphics
    turtle.setundobuffer(1)  # Optimize by reducing memory usage
    turtle.tracer(0)  # Turn off animation for instant drawing


def setup_keybindings(player: Player, missile: Missile) -> None:
    """
    Bind keyboard keys to player and missile actions to enable user interaction.

    Args:
        player (Any): The player object, which should have methods for movement and speed adjustment.
        missile (Any): The missile object, which should have a method to fire missiles based on current player position and heading.
    """
    turtle.onkey(player.turn_left, "Left")
    turtle.onkey(player.turn_left, "a")
    turtle.onkey(player.turn_right, "Right")
    turtle.onkey(player.turn_right, "d")
    turtle.onkey(player.accelerate, "Up")
    turtle.onkey(player.accelerate, "w")
    turtle.onkey(player.decelerate, "Down")
    turtle.onkey(player.accelerate, "s")
    turtle.onkey(
        lambda: missile.fire(player.xcor(), player.ycor(), player.heading()), "space"
    )
    turtle.listen()
