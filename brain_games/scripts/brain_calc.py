"""Brain-calc script."""
from brain_games import game_core
from brain_games.games import game_calc


def main():
    """Run brain-even game."""
    game_core.play_the_game(game_calc)


if __name__ == '__main__':
    main()
