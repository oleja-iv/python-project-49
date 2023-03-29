"""The maintenance of all games."""
import brain_games.cli


def start_the(game_name):
    """
    Start the game and check 4 results.

    Args:
        game_name: what game we will start
    """
    name = brain_games.cli.welcome_user()

    if game_name.is_winner():
        print('Congratulations, {who}!'.format(who=name))
    else:
        print("Let's try again, {who}!".format(who=name))
