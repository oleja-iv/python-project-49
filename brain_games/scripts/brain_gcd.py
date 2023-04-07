#!/usr/bin/env python3
"""Start the game 'even or not'."""
import brain_games.games.gcd
from brain_games.engine import start_game


def main():
    """Start the gcd game."""
    start_game(brain_games.games.gcd)


if __name__ == '__main__':
    main()
