"""Welcoming message."""

import prompt


def welcome_user():
    """Welcoming message."""
    return 'Welcome to the Brain Games!'


def get_username():
    """Get user's name."""
    user_name = prompt.string('May I have your name? ')
    return user_name
