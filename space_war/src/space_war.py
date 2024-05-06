import os
import turtle
import random
import time

turtle.fd(0)  # required by MacOS to show the window
turtle.speed(0)  # control the speed of the animation
turtle.bgcolor("black")  # background color
turtle.bgpic("./media/starfield.gif")
turtle.title("SpaceWar!")
turtle.ht()  # hide the default turtle
turtle.setundobuffer(1)  # saves memory
turtle.tracer(0)  # speeds up drawing


class Sprite(turtle.Turtle):
    def __init__(self, sprite_shape, color, start_x, start_y):
        turtle.Turtle.__init__(self, shape=sprite_shape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(start_x, start_y)
        self.speed = 1

    def move(self):
        """
        Move the sprites forward
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

    def is_collision(self, other):
        if (
            (self.xcor() >= (other.xcor() - 20))
            and (self.xcor() <= (other.xcor() + 20))
            and (self.ycor() >= (other.ycor() - 20))
            and (self.ycor() <= (other.ycor() + 20))
        ):
            return True
        return False


class Player(Sprite):
    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelarate(self):
        self.speed -= 1


class Enemy(Sprite):
    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.speed = 6
        self.setheading(random.randint(0, 360))


class Ally(Sprite):
    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.speed = 8
        self.setheading(random.randint(0, 360))

    def move(self):
        """
        Move the sprites forward
        """
        self.fd(self.speed)

        # Boundary detection

        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)


class Missile(Sprite):
    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.movement_speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)  # Initial off-screen position

    def fire(self):
        if self.status == "ready":
            # Play missile sound (ATM only for macos)
            os.system("afplay ./media/laser.mp3&")
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "ready":
            self.goto(-1000, 1000)

        if self.status == "firing":
            self.fd(self.movement_speed)

        # border check fixed
        if (
            self.xcor() < -290
            or self.xcor() > 290
            or self.ycor() > 290
            or self.ycor() < -290
        ):
            self.goto(-1000, 1000)
            self.status = "ready"


class Particle(Sprite):
    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000, -1000)  # Initial off-screen position
        self.frame = 0

    def explode(self, start_x, start_y):
        self.goto(start_x, start_y)
        self.setheading(random.randint(0, 360))
        self.frame = 1

    def move(self):
        if self.frame > 0 and self.frame <= 20:
            self.fd(10)
            self.frame += 1
        if self.frame > 20:
            self.frame = 0
            self.goto(-1000, -1000)


class Game:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        # Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = f"Score: {self.score}"
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))


# Create game object
game = Game()

# Draw the border
game.draw_border()

# show the game status
game.show_status()

# Instantiate
sprite_shape = "triangle"
color = "white"
start_x = 0
start_y = 0

# create my sprites
player = Player(
    sprite_shape=sprite_shape, color=color, start_x=start_x, start_y=start_y
)
# enemy = Enemy(sprite_shape="circle", color="red", start_x=-100, start_y=0)
missile = Missile(sprite_shape="triangle", color="yellow", start_x=0, start_y=0)
# ally = Ally(sprite_shape="square", color="blue", start_x=0, start_y=0)

enemies = []
for i in range(4):
    enemies.append(Enemy(sprite_shape="circle", color="red", start_x=-100, start_y=0))

allies = []
for i in range(4):
    allies.append(Ally(sprite_shape="square", color="blue", start_x=100, start_y=0))

particles = []

for i in range(20):
    particles.append(
        Particle(sprite_shape="circle", color="orange", start_x=0, start_y=0)
    )


# keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_left, "a")

turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.turn_right, "d")

turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.accelerate, "w")

turtle.onkey(player.decelarate, "Down")
turtle.onkey(player.accelerate, "s")

turtle.onkey(missile.fire, "space")

turtle.listen()

# Main game loop
while True:
    turtle.update()
    time.sleep(0.02)

    player.move()
    missile.move()

    for enemy in enemies:
        enemy.move()

        # Check for collision with the player
        if player.is_collision(enemy):
            # Play explosion sound (ATM only for macos)
            os.system("afplay ./media/explosion.mp3&")
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score -= 100
            game.show_status()

        # colission between missiles and enemy
        if missile.is_collision(enemy):
            # Play missile sound (ATM only for macos)
            os.system("afplay ./media/explosion.mp3&")
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = "ready"
            # increase the score
            game.score += 100
            game.show_status()
            # Do the explosion
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())

    for ally in allies:
        ally.move()

        # colission between missiles and ally
        if missile.is_collision(ally):
            # Play missile sound (ATM only for macos)
            os.system("afplay ./media/explosion.mp3&")
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            missile.status = "ready"
            # increase the score
            game.score -= 50
            game.show_status()

    for particle in particles:
        particle.move()
