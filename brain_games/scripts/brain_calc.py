"""Brain-calc script"""
from brain_games.games import game_calc
from brain_games import game_core


def main():
    """Run brain-even game"""
    game_core.play_the_game(game_calc)


if __name__ == '__main__':
    main()
