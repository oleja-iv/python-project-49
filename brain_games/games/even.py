"""Even game."""

import random

from brain_games.games.logic import is_correct_answer

rand = 30  # max value of in questions for even, progression and calc games


def give_a_task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def start_round():
    """
    Answer the question three times: even number or not.

    Returns:
         True if user is a winner, False in otherwise
    """
    rand_num = random.randint(-rand, rand)
    correct_answer = 'no' if rand_num % 2 else 'yes'
    if not is_correct_answer(rand_num, correct_answer):
        return False
    return True
