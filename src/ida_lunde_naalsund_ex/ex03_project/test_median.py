# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"


# Add comment that gives the source of the code

def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
            else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


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



def empty_list():
    """
    """



def original_data_unchanged():
    """
    """
    pass


def test_tuples():
    """
    """
    pass

