# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"


import pytest


def median(data):
    """
    Returns median of data.
    Source: https://bit.ly/2n5qLs4

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    s_data = sorted(data)
    n = len(s_data)
    if n == 0:
        raise ValueError
    else:
        return (s_data[n//2] if n % 2 == 1
                else 0.5 * (s_data[n//2 - 1] + s_data[n//2]))


def test_single():
    """Test that the median function
    returns the correct value for a one-element list.
    """
    assert median([1]) == 1


def test_odd_numbers():
    """Checks that the correct median is returned for
    lists with odd numbers of elements.
    """
    assert median([1, 2, 3, 4, 5]) == 3


def test_even_numbers():
    """Checks that the correct median is returned for
    lists with even numbers of elements.
    """
    assert median([1, 2, 3, 4]) == 2.5


def test_differently_ordered_elements():
    """Checks that the correct median is returned for
    list with ordered, reverse-ordered and unordered elements
    """
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([5, 4, 3, 2, 1]) == 3
    assert median([2, 4, 5, 3, 1]) == 3


def test_empty_list():
    """Checks that using an empty list
    raises an ValueError
    """
    with pytest.raises(ValueError):
        median([])


def test_original_data_unchanged():
    """Checks that the original data is unchanged
    """
    data = [1, 2, 3, 4, 5]
    median(data)

    assert data == [1, 2, 3, 4, 5]


def test_tuples():
    """Checks that function works for tuples
    """
    assert median((1, 2, 3, 4, 5)) == 3
