"""Brain-prime script."""
from brain_games import game_core
from brain_games.games import game_prime


def main():
    """Run brain-prime game."""
    game_core.play_the_game(game_prime)


if __name__ == '__main__':
    main()
