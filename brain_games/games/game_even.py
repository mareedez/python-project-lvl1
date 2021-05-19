"""Brain-even logic"""
from brain_games import game_core


def question():
    """Generate random number"""
    return game_core.random_number_generator()


def is_even(number):
    """Check if number is even"""
    if number % 2 == 0:
        return 'yes'
    return 'no'


def rules():
    """Game rules description"""
    return "Answer 'yes' if the number is even, otherwise answer 'no'\n"


def get_answers():
    """Get answer from user and correct answer"""
    number = question()
    correct_answer = is_even(number)
    user_answer = input('Question: {} '.format(number))
    print('Your answer:', user_answer)
    return correct_answer, user_answer
