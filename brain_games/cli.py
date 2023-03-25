"""All functions of the program."""


import prompt


def greet(who):
    """
    Greets person.

    Args:
        who: The person's name
    """
    print('Hello, {n}!'.format(n=who))


def welcome_greet():
    """Welcome greeting at the start of program."""
    print('Welcome to the Brain Games!')


def welcome_user():
    """Asks users to impute their name and greets them."""
    welcome_greet()
    name = prompt.string('May I have your name? ')
    greet(name)
