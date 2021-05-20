#!/usr/bin/env python3
"""Test module."""
import prompt


def welcome_user():
    """Ask for username and say Hello."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))


def main():
    """Brain-game main function."""
    welcome_user()


if __name__ == '__main__':
    main()
