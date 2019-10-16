# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"


def char_counts(textfilename):
    """Takes name of text file as input and
    counts the occurrences of each character
    in the text.

    :param textfilename: Name of file which
    characters we want to count
    :return: List with character codes with their
    corresponding number of occurrences.
    """
    text = open(textfilename).read()
    result = [0 for _ in range(256)]
    for char in text:
        char_code = ord(char)
        result[char_code] += 1

    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
