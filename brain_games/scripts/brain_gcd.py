"""Brain-gcd script."""
from brain_games import game_core
from brain_games.games import game_gcd


def main():
    """Run brain-even game."""
    game_core.play_the_game(game_gcd)


if __name__ == '__main__':
    main()
