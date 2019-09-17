# -*- coding: utf-8 -*-


def letter_freq(txt):
    """Function returns a dictionary with letters, symbols and digits
    from input "txt" as keys and counts as values.

    :param txt: Text written by user
    :return: freq
    """

    freq = {}

    for element in txt.lower():
        if element not in freq.keys():
            freq[element] = 1
        else:
            freq[element] += 1

    return freq


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
