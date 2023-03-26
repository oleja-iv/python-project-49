#!/usr/bin/env python3
"""
This is a simple command-line game.
Greets person
"""

from ..cli import welcome_user


def main():
    """File is loaded as script."""
    welcome_user()


if __name__ == '__main__':
    main()
