# -*- coding: utf-8 -*-

__author__ = 'Ida Lunde Naalsund'
__email__ = 'idna@nmbu.no'


from random import randint as rdint


def make_user_guess():
    """Makes user guess a number.
    :return: Guess made by user
    """
    user_guess = 0
    while user_guess < 1:
        user_guess = int(input('Your guess: '))
    return user_guess


def dice_throw():
    """Simulates two dice throws.
    :return: Random number between 2 and 12
    """
    return rdint(1, 6) + rdint(1, 6)


def compare_throw_and_guess(throw, guessed_number):
    """Checks if the user guess and the dice throws
    have the same value.
    :param throw: Dice throw
    :param guessed_number: Number guessed by user
    :return: True if the input elements equal each other, false otherwise.
    """
    return throw == guessed_number


if __name__ == '__main__':

    correct_answer = False
    points = 3
    dice_sum = dice_throw()
    while not correct_answer and points > 0:
        guess = make_user_guess()
        correct_answer = compare_throw_and_guess(dice_sum, guess)
        if not correct_answer:
            print('Wrong, try again!')
            points -= 1

    if points > 0:
        print('You won {} points.'.format(points))
    else:
        print('You lost. Correct answer: {}.'.format(dice_sum))
