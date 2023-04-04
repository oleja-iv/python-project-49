"""The maintenance of all games."""
import brain_games.cli


def start_the(game_name):
    """
    Start the game and check 4 results.

    Args:
        game_name: what game we will start
    """
    name = brain_games.cli.welcome_user()
    game_name.give_a_task()

    successful_rounds = 0
    while successful_rounds < 3:
        if not game_name.start_round():
            print("Let's try again, {who}!".format(who=name))
            break
        successful_rounds += 1
    if successful_rounds == 3:
        print('Congratulations, {who}!'.format(who=name))
