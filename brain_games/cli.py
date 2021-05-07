"""Welcoming message."""

import prompt


def welcome_user():
    """Says hello.

    Returns:
        greeting user by name
    """
    name = prompt.string('May I have your name? ')
    return 'Hello,', name
