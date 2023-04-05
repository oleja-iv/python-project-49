"""The maintenance of all games."""
import brain_games.cli
import prompt

MAX_ROUNDS = 3


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


def start_the(game_name):
    """
    Start the game and check 4 results.

    Args:
        game_name: what game we will start
    """
    name = brain_games.cli.welcome_user()
    game_name.give_a_task()

    successful_rounds = 0
    while successful_rounds < MAX_ROUNDS:
        task, correct_answer = game_name.start_round()
        if not is_correct_answer(task, correct_answer):
            print("Let's try again, {who}!".format(who=name))
            break
        successful_rounds += 1
    if successful_rounds == MAX_ROUNDS:
        print('Congratulations, {who}!'.format(who=name))
