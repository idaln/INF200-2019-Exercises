# -*- coding: utf-8 -*-

__author__ = 'Ida Lunde Naalsund'
__email__ = 'idna@nmbu.no'


def squares_by_comp(n):
    """Function squares the numbers in range of n that gives a remainder of 1
    when divided by 3, using a list comprehension.

    :param n: Number which range we want to be in
    :return: Squares of numbers
    """
    return [k ** 2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    """Function squares the numbers in range of n that gives a remainder of 1
    when divided by 3, using a for loop.

    :param n: Number which range we want to be in
    :return: Squares of numbers
    """
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k ** 2)
    return squares


if __name__ == '__main__':
    # We define an arbitrary number to run the test with
    test_n = 10
    if squares_by_loop(test_n) != squares_by_comp(test_n):
        print('ERROR!')
