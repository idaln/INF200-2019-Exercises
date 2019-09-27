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


# def test_empty_list(self):
#  """Checks that using an empty list
#  raises an ValueError
#  """
#  self.assertRaises(IndexError, median([]))
#  pass


def test_original_data_unchanged():
    """Checks that the original data is unchanged
    """
    data = [1, 2, 3, 4, 5]
    med_data = median(data)

    assert data == [1, 2, 3, 4, 5]


def test_tuples():
    """Checks that function works for tuples
    """
    assert median((1, 2, 3, 4, 5)) == 3



