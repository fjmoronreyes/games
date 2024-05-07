import turtle
import time
import random

delay = 0.1

# Scores
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off screen updates for manual update

# Snake head
head = turtle.Turtle()
head.speed(0)  # Animation speed (not movement speed)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

# List to store segments of the snake's body
segments = []

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.shape("square")
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(
    "Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal")
)


# Functions for movement
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for collision with the border
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
        delay = 0.1
        score_display.clear()
        score_display.write(
            "Score: {}  High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score

        score_display.clear()
        score_display.write(
            "Score: {}  High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

        # Decrease the delay (increase game speed)
        delay -= 0.001

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if segments:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            score_display.clear()
            score_display.write(
                "Score: {}  High Score: {}".format(score, high_score),
                align="center",
                font=("Courier", 24, "normal"),
            )

    time.sleep(delay)

wn.mainloop()
