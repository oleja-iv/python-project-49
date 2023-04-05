"""Your mind is calculator game."""
import operator
import random

RANDOM_LIMIT = 30  # max value of operands
# dict with operators for calc game
action = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def give_a_task():
    """Show a task."""
    print('What is the result of the expression?')


def start_round():
    """
    Generate expression and correct answer for it.

    Returns:
         expression: task that should be resolved
         correct_answer: correct answer for the task
    """
    first_operand = random.randint(-RANDOM_LIMIT, RANDOM_LIMIT)
    second_operand = random.randint(-RANDOM_LIMIT, RANDOM_LIMIT)
    sign = random.choice(('+', '-', '*'))

    correct_answer = str(
        action[sign](first_operand, second_operand),
    )
    expression = '{first} {s} {second}'.format(
        first=first_operand,
        s=sign,
        second=second_operand,
    )

    return expression, correct_answer
