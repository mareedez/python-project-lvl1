"""Brain-even logic"""
import random
import sys
import prompt


def get_username():
    """Get name from input"""
    user_name = prompt.string('May I have your name? ')
    return user_name


def question():
    """Generate random number"""
    return random.randint(0, 100)


def is_even(number):
    """Check if number is even"""
    if number % 2 == 0:
        return 'yes'
    return 'no'


def rules():
    """Game rules description"""
    return "Answer 'yes' if the number is even, otherwise answer 'no'\n"


def get_answers(number):
    """Get answer from user and correct answer"""
    correct_answer = is_even(number)
    user_answer = input('Question: {} '.format(number))
    print('Your answer:', user_answer)
    return correct_answer, user_answer


def play_the_game():
    """Main game script"""
    user_name = get_username()
    print('Welcome, {}!'.format(user_name))
    trials = 3
    print(rules())
    while trials:
        correct_answer, user_answer = get_answers(question())
        if correct_answer == user_answer:
            print("Correct!\n")
            trials -= 1
            continue
        print("'{}' is wrong answer. Correct answer was '{}'.".format(user_answer, correct_answer))
        print('Let\'s try again,', user_name)
        sys.exit()
    print("Congratulations, {}!".format(user_name))
