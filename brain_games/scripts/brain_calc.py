#!/usr/bin/env python3
"""Start the game 'calc it'."""
import brain_games.games.calc
from brain_games.engine import start_game


def main():
    """Start the calc game."""
    start_game(brain_games.games.calc)


if __name__ == '__main__':
    main()
