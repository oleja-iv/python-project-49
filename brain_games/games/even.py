"""Even game."""

import random

RANDOM_LIMIT = 30  # max value of in questions for even, progression and calc games


def give_a_task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def start_round():
    """
    Generate even or not number and solution.

    Returns:
         random_number: task that should be resolved
         correct_answer: correct answer for the task
    """
    random_number = random.randint(-RANDOM_LIMIT, RANDOM_LIMIT)
    correct_answer = 'no' if random_number % 2 else 'yes'
    return random_number, correct_answer
