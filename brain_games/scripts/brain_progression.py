"""Brain-progression script."""
from brain_games import game_core
from brain_games.games import game_progression


def main():
    """Run brain-even game."""
    game_core.play_the_game(game_progression)


if __name__ == '__main__':
    main()
