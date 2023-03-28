"""Find the greatest common divider game."""
import math
import random

from brain_games.games.logic import is_correct_answer

rand = 15  # max value of start dividers in gcd game


def generate_the_pair():
    """
    Generate a pair with common divider.

    Returns:
         Tuple with pair
    """
    num1 = random.randint(0, rand)
    num2 = random.randint(0, rand)
    num3 = random.randint(0, rand)
    first = num1 * num3
    second = num2 * num3

    return first, second


def is_winner():
    """
    Answer the question three times, find the greatest common divisor.

    Returns:
         True if user is a winner, False in otherwise
    """
    print('Find the greatest common divisor of given numbers.')
    for _ in range(0, 3):
        first, second = generate_the_pair()

        correct_answer = str(math.gcd(first, second))
        pair = '{x} {y}'.format(x=first, y=second)

        if not is_correct_answer(pair, correct_answer):
            return False
    return True
