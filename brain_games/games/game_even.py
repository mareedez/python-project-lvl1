"""Brain-even logic."""
from brain_games import game_core


def question():
    """Generate number from question.

    Returns:
         integer in range from 1 to 100
    """
    return game_core.generate_random_number()


def is_even(number):
    """Check if number is even.

    Args:
        number: integer number

    Returns:
        'yes' if number is even else 'no'
    """
    if number % 2 == 0:
        return 'yes'
    return 'no'


def rules():
    """Even-game rules description.

    Returns:
        gameplay guidance
    """
    return "Answer 'yes' if the number is even, otherwise answer 'no'\n"


def get_answers():
    """Get answer from user and correct answer.

    Returns:
        correct_answer: expected answer
        user_answer: answer entered by the user
    """
    number = question()
    correct_answer = is_even(number)
    user_answer = input('Question: {0} '.format(number))
    print('Your answer:', user_answer)
    return correct_answer, user_answer
