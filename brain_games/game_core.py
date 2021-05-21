"""Game engine."""
import random
import sys

import prompt


def get_username():
    """Get name from input.

    Returns:
        user_name
    """
    return prompt.string('May I have your name? ')


def generate_random_number():
    """Create random number.

    Returns:
        number in range from 1 to 100
    """
    return random.randint(1, 100)


def play_the_game(game):
    """Run the main game script.

    Args:
        game: run selected game from the games folder
    """
    user_name = get_username()
    print('Welcome, {0}!'.format(user_name))
    trials = 3
    print(game.rules())
    while trials:
        correct_answer, user_answer = game.get_answers()
        if correct_answer == user_answer:
            print('Correct!')
            trials -= 1
            continue
        message = "'{0}' is wrong answer. Correct answer was '{1}'."
        print(message.format(user_answer, correct_answer))
        print("Let's try again, {0}!".format(user_name))
        sys.exit()
    print('Congratulations, {0}!'.format(user_name))
