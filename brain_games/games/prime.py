"""Answer: the given number is prime, or not."""
import math
import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANDOM_LIMIT = 100  # max value of number


def is_prime(given_number):
    """
    Check number is prime or not.

    Args:
        given_number: number that would checked

    Returns:
         True if number is Prime, otherwise False
    """
    max_divider = int(math.sqrt(given_number)) + 1
    # max divider < sqrt(not_prime)

    for element in range(2, max_divider):
        if given_number % element == 0:
            return False
    return True


def get_game():
    """
    Answer 'yes' if number is prime, otherwise 'no'.

    Returns:
         random_number: we check it for 'Prime'
         correct_answer: 'yes', if number is Prime, otherwise 'no'
    """
    random_number = random.randint(2, RANDOM_LIMIT)
    correct_answer = 'yes' if is_prime(random_number) else 'no'

    return random_number, correct_answer
