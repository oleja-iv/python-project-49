#!/usr/bin/env python3
"""
This is a simple command-line game.

Greets person and start the game "even or not"
"""
from brain_games.cli import welcome_user
from brain_games.even import is_winner_in_even_game


def main():
    """Start the game."""
    name = welcome_user()
    if is_winner_in_even_game():
        print('Congratulations, {who}!'.format(who=name))
    else:
        print("Let's try again, {who}!".format(who=name))


if __name__ == '__main__':
    main()
