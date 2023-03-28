"""Common functions from all games."""

import prompt


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
