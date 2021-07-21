"""Brain-gcd logic."""
from math import gcd

from brain_games import game_core


def question():
    """Generate math problem elements.

    Returns:
        first_number, second_number: random integers
    """
    return game_core.generate_random_number()


def rules():
    """Gcd-game rules description.

    Returns:
        gameplay guidance
    """
    return 'Find the greatest common divisor of given numbers.\n'

def is_prime(num):
    """Check if number is prime.

    Args:
        num: integer number

    Returns:
        'yes' if number is prime else 'no'
    """
    if num < 2:
        return 'no'
    res = 0
    for index in range(2, num // 2 + 1):
        if num % index == 0:
            res = res + 1
    if res <= 0:
        return 'yes'
    return 'no'


def get_answers():
    """Get answer from user and correct answer.

    Returns:
        correct_answer: expected answer
        user_answer: answer entered by the user
    """
    number = question()
    correct_answer = is_prime(number)
    print('Question: {0}'.format(str(number)))
    user_answer = input('Your answer: ')
    return correct_answer, user_answer
