#!/usr/bin/env python3
"""Start the game 'prime or not'."""
import brain_games.games.prime
from brain_games.engine import start_the


def main():
    """Start the progression game."""
    start_the(brain_games.games.prime)


if __name__ == '__main__':
    main()
