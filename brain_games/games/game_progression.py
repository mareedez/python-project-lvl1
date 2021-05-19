"""Brain-progression logic."""
import random

from brain_games import game_core


def question():
    """Generate arithmetic progression.

    Returns:
        progression sequence as list of 10 integers
    """
    first_number = game_core.generate_random_number()
    progression_step = random.randint(2, 9)
    sequence = []
    for _ in range(10):
        sequence.append(str(first_number))
        first_number += progression_step
    return sequence


def rules():
    """Progression-game rules description.

    Returns:
        gameplay guidance
    """
    return 'What number is missing in the progression?\n'


def get_answers():
    """Get answer from user and correct answer.

    Returns:
        correct_answer: expected answer
        user_answer: answer entered by the user
    """
    sequence = question()
    correct_answer = random.choice(sequence)
    sequence_to_show = ' '.join(sequence).replace(correct_answer, '..')
    quest = 'Question: {0} '
    user_answer = input(quest.format(sequence_to_show))
    print('Your answer:', user_answer)
    return correct_answer, user_answer
