"""Even game."""

import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
RANDOM_LIMIT = 30  # max value of random number


def is_even(number):
    """
    Check number is even or not.

    Args:
        number: generated random number

    Returns:
        True if number is even, otherwise False
    """
    return not number % 2


def start_round():
    """
    Generate even or not number and solution.

    Returns:
         random_number: task that should be resolved
         correct_answer: correct answer for the task
    """
    random_number = random.randint(-RANDOM_LIMIT, RANDOM_LIMIT)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return random_number, correct_answer
