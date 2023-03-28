"""Your mind is calculator game."""
import operator
import random

from brain_games.games.logic import is_correct_answer

rand = 30  # max value of operands
# dict with operators 4 calc game
action = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def is_winner():
    """
    Answer the question three times: what is the result of the expression.

    Returns:
         True if user is a winner, False in otherwise
    """
    print('What is the result of the expression?')
    for _ in range(0, 3):
        first = random.randint(-rand, rand)
        second = random.randint(-rand, rand)
        sign = random.choice(('+', '-', '*'))

        correct_answer = str(action[sign](first, second))
        expression = '{x} {s} {y}'.format(x=first, s=sign, y=second)

        if not is_correct_answer(expression, correct_answer):
            return False
    return True
