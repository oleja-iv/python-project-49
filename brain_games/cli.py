"""Greeting module."""


import prompt


def welcome_user():
    """
    Asks users to impute their name and greets them.

    Returns:
        The user's name as string
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {who}!'.format(who=name))
    return name
