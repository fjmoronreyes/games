# SpaceWar! - Version 1

SpaceWar! is a Python-based space shooter game where players navigate a spaceship, avoid collisions with enemies, shoot missiles, and collect points. This project is a modern take on classic arcade space shooters, implemented with Python and the `turtle` module.

## Project Structure

The project is organized into several Python files, each handling specific aspects of the game:

- `space_war.py`: The main game file that runs the game loop and initializes the game setup.
- `sprite.py`: Defines the `Sprite` class, which is the base class for all movable objects in the game.
- `player.py`: Contains the `Player` class that defines player-specific attributes and methods.
- `enemy.py`: Contains the `Enemy` class for enemy attributes and behaviors.
- `ally.py`: Contains the `Ally` class which manages friendly units that appear in the game.
- `missile.py`: Manages the missiles that the player can fire.
- `particle.py`: Defines the `Particle` class for explosion effects.
- `game_logic.py`: Manages game state, score, and other game-specific functionalities.
- `game_interface.py`: Handles the game window setup and user input bindings.
- `utils.py`: Includes utility functions like playing sounds and managing collisions.

## Author

**Fco J Moron**

## Acknowledgments

**Kudos to:**

- **Wynand1004 (GitHub)** - I want to give a special thanks to Wynand1004 and his tutorials on TokyoEdtech YouTube channel.

## How to Run

To play SpaceWar!, ensure you have Python and the `turtle` module installed on your computer. You can run the game by navigating to the project directory and executing:

```bash
python space_war.py
