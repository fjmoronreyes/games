import turtle


def update_screen():
    turtle.update()


def setup_screen():
    turtle.fd(0)  # Required by MacOS to show the window
    turtle.speed(0)  # Control the speed of the animation
    turtle.bgcolor("black")  # Background color
    turtle.bgpic("../media/starfield.gif")  # Background image
    turtle.title("SpaceWar!")  # Set window title
    turtle.ht()  # Hide the default turtle
    turtle.setundobuffer(1)  # Saves memory
    turtle.tracer(0)  # Speeds up drawing


def setup_keybindings(player, missile):
    turtle.onkey(player.turn_left, "Left")
    turtle.onkey(player.turn_left, "a")
    turtle.onkey(player.turn_right, "Right")
    turtle.onkey(player.turn_right, "d")
    turtle.onkey(player.accelerate, "Up")
    turtle.onkey(player.accelerate, "w")
    turtle.onkey(player.decelarate, "Down")
    turtle.onkey(player.accelerate, "s")
    turtle.onkey(
        lambda: missile.fire(player.xcor(), player.ycor(), player.heading()), "space"
    )
    turtle.listen()
