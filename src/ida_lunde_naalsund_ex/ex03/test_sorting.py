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
    list_data = list(data)
    n = len(list_data)

    while n > 0:
        i = 1
        while i < n:
            if list_data[i] < list_data[i-1]:
                list_data[i], list_data[i-1] = list_data[i-1], list_data[i]
            i += 1
        n -= 1
    return list_data


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []
    assert bubble_sort(()) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    assert sorted_data is not data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    bubble_sort(data)

    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""

    data = [1, 2, 3]
    sorted_data = bubble_sort(data)

    assert sorted_data == data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    assert sorted_data == [1, 2, 3]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""

    data = [1, 1, 1]
    sorted_data = bubble_sort(data)

    assert sorted_data == data


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    assert bubble_sort([2, 6, 3, 8, 1]) == [1, 2, 3, 6, 8]
    assert bubble_sort([2, 6, 3, 8, 1, 5, 4]) == [1, 2, 3, 4, 5, 6, 8]
    assert bubble_sort(['2', '4', '1', '5']) == ['1', '2', '4', '5']
    assert bubble_sort(['b', 'h', 'j', 'a']) == ['a', 'b', 'h', 'j']
    assert bubble_sort(['you', 'are', 'cool']) == ['are', 'cool', 'you']
