"""Answer: the given number is prime, or not."""
import math
import random

from brain_games.games.logic import is_correct_answer

rand = 100  # max value of number


def give_a_task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def check(given_number):
    """
    Check number is prime or not.

    Args:
        given_number: number that would checked

    Returns:
         True or False
    """
    max_divider = int(math.sqrt(given_number)) + 1
    # max divider < sqrt(not prime)

    for element in range(2, max_divider):
        if given_number % element == 0:
            return False
    return True


def start_round():
    """
    Answer 'yes' if number is prime, otherwise 'no'.

    Returns:
         True if user is a winner, False in otherwise
    """
    number = random.randint(2, rand)
    correct_answer = 'yes' if check(number) else 'no'

    if not is_correct_answer(number, correct_answer):
        return False
    return True
