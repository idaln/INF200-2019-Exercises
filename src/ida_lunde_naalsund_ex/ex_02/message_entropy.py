# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"

import math


def letter_freq(txt):
    """Takes a string as input and returns a dictionary
    with characters in string as keys and number of
    occurrences as values.

    :param txt: String written by user.
    :return: Dictionary with characters as keys
    and number of occurrences as values.
    """

    freq = {}

    for element in txt:
        if element not in freq.keys():
            freq[element] = 1
        else:
            freq[element] += 1

    return freq


def entropy(message):
    """Takes string as input and returns
    the entropy of the string.

    :param message: String given by user.
    :return: The entropy of the given string.
    """

    occurrence_dict = letter_freq(message)
    n = len(message)

    message_entropy = 0
    for count in occurrence_dict.values():
        message_entropy += (count/n) * math.log2(count/n)

    return -message_entropy


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
