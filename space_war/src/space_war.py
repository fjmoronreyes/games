import time
from sprite import Sprite
from enemy import Enemy
from player import Player
from ally import Ally
from particle import Particle
from missile import Missile
from game_logic import Game
from game_interface import update_screen, setup_screen, setup_keybindings
from utils import play_sound, manage_collision


def initialize_game():
    """Sets up the game environment and entities."""
    setup_screen()
    game = Game()
    game.draw_border()
    game.show_status()

    player = Player("triangle", "white", 0, 0)
    missile = Missile("triangle", "yellow", 0, 0)
    enemies = [Enemy("circle", "red", -100, 0) for _ in range(4)]
    allies = [Ally("square", "blue", 100, 0) for _ in range(4)]
    particles = [Particle("circle", "orange", 0, 0) for _ in range(20)]

    setup_keybindings(player, missile)
    return game, player, missile, enemies, allies, particles


def main():
    # Main game loop

    game, player, missile, enemies, allies, particles = initialize_game()

    while True:
        update_screen()
        time.sleep(0.02)
        player.move()
        missile.move()

        # Process movements and collisions for enemies
        for enemy in enemies:
            enemy.move()
            if player.is_collision(enemy):
                manage_collision(enemy)
                game.update_score(-100)
            if missile.is_collision(enemy):
                manage_collision(enemy)
                missile.status = "ready"
                game.update_score(100)
                for particle in particles:
                    particle.explode(missile.xcor(), missile.ycor())

        # Process movements and collisions for allies
        for ally in allies:
            ally.move()
            if missile.is_collision(ally):
                manage_collision(ally)
                missile.status = "ready"
                game.update_score(-50)

        # Update particle movements
        for particle in particles:
            particle.move()


if __name__ == "__main__":
    main()
