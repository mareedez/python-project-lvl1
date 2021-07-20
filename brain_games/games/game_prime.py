"""Brain-prime logic."""
from brain_games import game_core
from sympy import isprime


def question():
    """Generate random number.

    Returns:
        number: integer in range from 1 to 100
    """
    return game_core.generate_random_number()


def is_prime(number):
    """Check if number is prime.

    Args:
        number: integer number

    Returns:
        'yes' if number is prime else 'no'
    """
    if isprime(number):
        return 'yes'
    return 'no'


def rules():
    """Prime-game rules description.

    Returns:
        gameplay guidance
    """
    return 'Answer "yes" if given number is prime. Otherwise answer "no"./n'


def get_answers():
    """Get answer from user and calculate correct answer.

    Returns:
        correct_answer: expected answer
        user_answer: answer entered by the user
    """
    number = question()
    correct_answer = is_prime(number)
    print('Question: {0}'.format(str(number)))
    user_answer = input('Your answer: ')
    return correct_answer, user_answer
