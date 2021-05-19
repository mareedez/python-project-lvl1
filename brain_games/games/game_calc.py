"""Brain-calc logic."""
import operator
import random

from brain_games import game_core

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def question():
    """Generate math problem elements.

    Returns:
        first_number, second_number: random integers
        random_operator: operator '-', '+', '*'
    """
    first_number = game_core.generate_random_number()
    second_number = game_core.generate_random_number()
    operation = random.choice(list(OPERATORS.keys()))
    return first_number, second_number, operation


def rules():
    """Calc-game rules description.

    Returns:
        gameplay guidance
    """
    return 'What is the result of the expression?\n'


def get_answers():
    """Get answer from user and correct answer.

    Returns:
        correct_answer: expected answer
        user_answer: answer entered by the user
    """
    first_number, second_number, operation = question()
    correct_answer = str(OPERATORS.get(operation)(first_number, second_number))
    quest = 'Question: {0} {1} {2} '
    user_answer = input(quest.format(first_number, operation, second_number))
    print('Your answer:', user_answer)
    return correct_answer, user_answer
