#!/usr/bin/env python3
"""Start the game 'find the missing element of progression'."""
import brain_games.games.progression
from brain_games.engine import start_game


def main():
    """Start the progression game."""
    start_game(brain_games.games.progression)


if __name__ == '__main__':
    main()
