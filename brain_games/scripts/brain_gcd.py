#!/usr/bin/env python3
"""Start the game 'even or not'."""
import brain_games.games.gcd
from brain_games.launch import start_the


def main():
    """Start the gcd game."""
    start_the(brain_games.games.gcd)


if __name__ == '__main__':
    main()
