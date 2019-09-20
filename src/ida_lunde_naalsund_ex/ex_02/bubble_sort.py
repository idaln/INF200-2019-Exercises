# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"


def bubble_sort(data):
    """Takes a list or tuple of numbers as input.
    Returns a copy of the list where the numbers are
    sorted in increasing order. 

    :param data: List or tuple containing numbers.
    :return: Sorted list.
    """
    copy = list(data)
    n = len(copy)

    while n > 0:
        i = 1
        while i < n:
            if copy[i] < copy[i-1]:
                copy[i], copy[i-1] = copy[i-1], copy[i]
            i += 1
        n -= 1
    return copy


if __name__ == "__main__":

    for element in ((),
                    (1,),
                    (1, 3, 8, 12),
                    (12, 8, 3, 1),
                    (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(element, bubble_sort(element)))
