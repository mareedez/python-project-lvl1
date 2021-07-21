"""Brain-gcd logic."""
from math import gcd

from brain_games import game_core


def question():
    """Generate math problem elements.

    Returns:
        first_number, second_number: random integers
    """
    first_number = game_core.generate_random_number()
    second_number = game_core.generate_random_number()
    return first_number, second_number


def rules():
    """Gcd-game rules description.

    Returns:
        gameplay guidance
    """
    return 'Find the greatest common divisor of given numbers.\n'


def get_answers():
    """Get answer from user and correct answer.

    Returns:
        correct_answer: expected answer
        user_answer: answer entered by the user
    """
    first_number, second_number = question()
    correct_answer = str(gcd(first_number, second_number))
    quest = 'Question: {0} {1} '
    user_answer = input(quest.format(first_number, second_number))
    print('Your answer:', user_answer)
    return correct_answer, user_answer
