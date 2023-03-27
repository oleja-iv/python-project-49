"""The logic of all games."""
import operator
import random

import prompt
from brain_games.cli import welcome_user

range_ = 30  # max value of numbers in questions
# dict with operators
action = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def is_correct_answer(question, correct_answer):
    """
    Ask a question and check answer.

    Args:
        question: what the user has to solve
        correct_answer: correct answer

    Returns:
        True if answer is correct, false in otherwise
    """
    print('Question: {qstn}'.format(qstn=question))
    answer = prompt.string('Your answer: ')

    if answer == correct_answer:
        print('Correct!')
        return True

    print(
        "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'.".format(
            wrong=answer, correct=correct_answer,
        ))
    return False


def is_winner_in_even_game():
    """
    Answer the question three times: even number or not.

    Returns:
         True if user is a winner, False in otherwise
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(0, 3):
        rand_num = random.randint(--range_, range_)
        correct_answer = 'no' if rand_num % 2 else 'yes'
        if not is_correct_answer(rand_num, correct_answer):
            return False
    return True


def is_winner_in_calc_game():
    """
    Answer the question three times: what is the result of the expression.

    Returns:
         True if user is a winner, False in otherwise
    """
    print('What is the result of the expression?')
    for _ in range(0, 3):
        first = random.randint(-range_, range_)
        second = random.randint(-range_, range_)
        sign = random.choice(('+', '-', '*'))

        correct_answer = str(action[sign](first, second))
        expression = '{x} {s} {y}'.format(x=first, s=sign, y=second)

        if not is_correct_answer(expression, correct_answer):
            return False
    return True


def start_the(game_name):
    """
    Start the game and check 4 results.

    Args:
        game_name: what game we will start
    """
    name = welcome_user()
    games = {
        'even_game': is_winner_in_even_game,
        'calc_game': is_winner_in_calc_game,
    }

    is_winner = games[game_name]()  # Не стал упрощать и пихать в if
    if is_winner:
        print('Congratulations, {who}!'.format(who=name))
    else:
        print("Let's try again, {who}!".format(who=name))
