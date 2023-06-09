"""The maintenance of all games."""
import brain_games.cli
import prompt

MAX_ROUNDS = 3


def start_game(game_name):
    """
    Start the game and check 4 results.

    Args:
        game_name: what game we will start
    """
    name = brain_games.cli.welcome_user()
    print(game_name.GAME_RULE)

    successful_rounds = 0
    while successful_rounds < MAX_ROUNDS:
        question, correct_answer = game_name.get_game()
        print('Question: {qstn}'.format(qstn=question))
        answer = prompt.string('Your answer: ')

        if answer != correct_answer:
            print(
                "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'.".
                format(wrong=answer, correct=correct_answer),
            )
            print("Let's try again, {who}!".format(who=name))
            return
        print('Correct!')
        successful_rounds += 1
    print('Congratulations, {who}!'.format(who=name))
