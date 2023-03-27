"""The logic of all games."""

from random import randint
from brain_games.cli import welcome_user

import prompt


def is_correct_answer(question, correct_answer):
    """
    Ask a question and check answer.

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
        rand_num = randint(-100, 100)
        correct_answer = 'no' if rand_num % 2 else 'yes'
        if not is_correct_answer(rand_num, correct_answer):
            return False
    return True


def start_the(game_name):
    name = welcome_user()
    # is_winner = True  # U R always a winner =) Linter whant it

    games = {
        'even_game': is_winner_in_even_game
    }

    is_winner = games[game_name]()  # Не стал упрощать и пихать в if
    if is_winner:
        print('Congratulations, {who}!'.format(who=name))
    else:
        print("Let's try again, {who}!".format(who=name))