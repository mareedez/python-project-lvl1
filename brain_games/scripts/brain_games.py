#!/usr/bin/env python3
"""Welcoming message."""

from brain_games.cli import welcome_user


def main():
    """Take user's name and greet him."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
