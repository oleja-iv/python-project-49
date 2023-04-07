"""Find the greatest common divider game."""
import math
import random

GAME_RULE = 'Find the greatest common divisor of given numbers.'
RANDOM_LIMIT = 15  # max value of start dividers in gcd game


def generate_gcd_pair():
    """
    Generate a pair with common divider.

    Returns:
         Tuple with pair
    """
    random_num1 = random.randint(0, RANDOM_LIMIT)
    random_num2 = random.randint(0, RANDOM_LIMIT)
    common_divider = random.randint(0, RANDOM_LIMIT)

    first_pseudo_random = random_num1 * common_divider
    second_pseudo_random = random_num2 * common_divider

    return first_pseudo_random, second_pseudo_random


def get_game():
    """
    Answer the question three times, find the greatest common divisor.

    Returns:
         pair: two numbers, where user will find the gcd
         correct_answer: correct answer
    """
    first_random_number, second_random_number = generate_gcd_pair()

    correct_answer = str(math.gcd(first_random_number, second_random_number))
    pair = '{x} {y}'.format(x=first_random_number, y=second_random_number)

    return pair, correct_answer
