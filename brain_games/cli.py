import prompt


def greet(who):
    print(f'Hello, {who}!')


def welcome_greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    welcome_greet()
    name = prompt.string('May I have your name? ')
    greet(name)