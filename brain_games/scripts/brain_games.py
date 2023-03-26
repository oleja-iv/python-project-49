#!/usr/bin/env python3
"""
This is a simple command-line game.

Asks person for name greets them
"""

from brain_games.cli import welcome_user


def main():
    """File is loaded as script, greet the person."""
    welcome_user()


if __name__ == '__main__':
    main()
