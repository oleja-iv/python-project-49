"""The maintenance of all games."""
import brain_games.cli
import brain_games.games.calc
import brain_games.games.even
import brain_games.games.gcd
import brain_games.games.prime
import brain_games.games.progression


def start_the(game_name):
    """
    Start the game and check 4 results.

    Args:
        game_name: what game we will start
    """
    name = brain_games.cli.welcome_user()
    game = {
        'even_game': brain_games.games.even.is_winner,
        'calc_game': brain_games.games.calc.is_winner,
        'gcd_game': brain_games.games.gcd.is_winner,
        'progression_game': brain_games.games.progression.is_winner,
        'prime_game': brain_games.games.prime.is_winner,
    }

    is_winner = game[game_name]()
    if is_winner:
        print('Congratulations, {who}!'.format(who=name))
    else:
        print("Let's try again, {who}!".format(who=name))
