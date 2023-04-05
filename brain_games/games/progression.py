"""Find the missing value of progression game."""
import random

RANDOM_STEP_LIMIT = 20  # max value of step in progression game
RANDOM_LIMIT = 1000  # max start value
(MINIMUM_SIZE, MAXIMUM_SIZE) = (5, 10)  # amount of numbers in shown progression


def give_a_task():
    """Show a task."""
    print('What number is missing in the progression?')


def generate_progression():
    """
    Generate progression.

    Returns:
         list of progression
    """
    element = random.randint(-RANDOM_LIMIT, RANDOM_LIMIT)
    length = random.randint(MINIMUM_SIZE, MAXIMUM_SIZE)
    step = random.randint(-RANDOM_STEP_LIMIT, RANDOM_STEP_LIMIT)

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
    progression, length = generate_progression()
    element = random.randint(0, length)
    missing_number = progression[element]
    progression[element] = '..'
    progression_as_string = ' '.join(progression)

    return progression_as_string, missing_number
