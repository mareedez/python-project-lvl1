"""Brain-even script."""
from brain_games import game_core
from brain_games.games import game_even


def main():
    """Run brain-even game."""
    game_core.play_the_game(game_even)


if __name__ == '__main__':
    main()
