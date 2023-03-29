#!/usr/bin/env python3
"""Start the game 'find the missing element of progression'."""
import brain_games.games.progression
from brain_games.launch import start_the


def main():
    """Start the progression game."""
    start_the(brain_games.games.progression)


if __name__ == '__main__':
    main()
