"""Brain-calc logic"""
import random
import operator
from brain_games import game_core

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def question():
    """Generate random calculations"""
    number_1 = game_core.random_number_generator()
    number_2 = game_core.random_number_generator()
    random_operator = random.choice(list(OPERATORS.keys()))
    return number_1, number_2, random_operator


def rules():
    """Game rules description"""
    return "What is the result of the expression?\n"


def get_answers():
    """Get answer from user and correct answer"""
    number_1, number_2, random_operator = question()
    correct_answer = str(OPERATORS.get(random_operator)(number_1, number_2))
    user_answer = input('Question: {} {} {} '.format(number_1, random_operator, number_2))
    print('Your answer:', user_answer)
    return correct_answer, user_answer
