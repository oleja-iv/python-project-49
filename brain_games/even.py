"""The logic of the even game."""

from random import randint

import prompt


def question():
    """
    Ask a question even number or not.

    Returns:
        True if answer is correct, false in otherwise
    """
    rand_num = randint(-100, 100)
    print('Question: {rand}'.format(rand=rand_num))
    answer = prompt.string('Your answer: ')

    correct_answer = 'no' if rand_num % 2 else 'yes'

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
    Answer for three questions: even number or not.

    Returns:
         True if user is a winner, False in otherwise
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(0, 3):
        if not question():
            return False
    return True
