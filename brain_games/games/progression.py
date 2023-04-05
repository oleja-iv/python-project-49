"""Find the missing value of progression game."""
import random

rand_step = 20  # max value of step in progression game
rand = 1000  # max start value
(min_p, max_p) = (5, 10)  # amount of numbers in shown progression


def give_a_task():
    print('What number is missing in the progression?')


def generate():
    """
    Generate progression.

    Returns:
         list of progression
    """
    element = random.randint(-rand, rand)
    length = random.randint(min_p, max_p)
    step = random.randint(-rand_step, rand_step)
    progression = [str(element)]
    for _ in range(0, length):
        element += step
        progression.append(str(element))
    return progression, length


def start_round():
    """
    Answer the question three times, find the missing element in progression.

    Returns:
         True if user is a winner, False in otherwise
    """
    progression, length = generate()
    element = random.randint(0, length)
    number = progression[element]
    progression[element] = '..'
    prog_str = ' '.join(progression)

    return prog_str, number
