#!/usr/bin/env python3
"""Start the game 'calc it'."""
import brain_games.games.calc
from brain_games.launch import start_the


def main():
    """Start the calc game."""
    start_the(brain_games.games.calc)


if __name__ == '__main__':
    main()
