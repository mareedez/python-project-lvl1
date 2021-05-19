"""Game engine"""
import sys
import random
import prompt


def get_username():
    """Get name from input"""
    user_name = prompt.string('May I have your name? ')
    return user_name


def random_number_generator():
    """Creates random number"""
    return random.randint(1, 100)


def play_the_game(game):
    """Main game script"""
    user_name = get_username()
    print('Welcome, {}!'.format(user_name))
    trials = 3
    print(game.rules())
    while trials:
        correct_answer, user_answer = game.get_answers()
        if correct_answer == user_answer:
            print("Correct!\n")
            trials -= 1
            continue
        print("'{}' is wrong answer. Correct answer was '{}'.".format(user_answer, correct_answer))
        print('Let\'s try again,', user_name)
        sys.exit()
    print("Congratulations, {}!".format(user_name))
