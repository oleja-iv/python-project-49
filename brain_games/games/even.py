"""Even game."""

import random

RANDOM_LIMIT = 30  # max value of random number


def give_a_task():
    """Show a task."""
    print('Answer "yes" if the number is even, otherwise answer "no".')


def check_for_even(number):
    """
    Check number is even or not.

    Args:
        number: generated random number

    Returns:
        'yes' if number is even, otherwise 'no'
    """
    return 'no' if number % 2 else 'yes'


def start_round():
    """
    Generate even or not number and solution.

    Returns:
         random_number: task that should be resolved
         correct_answer: correct answer for the task
    """
    random_number = random.randint(-RANDOM_LIMIT, RANDOM_LIMIT)
    correct_answer = check_for_even(random_number)
    return random_number, correct_answer
