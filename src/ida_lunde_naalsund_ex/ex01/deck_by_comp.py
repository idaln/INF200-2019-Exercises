
# -*- coding: utf-8 -*-

SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    """Function creates a deck of cards
    with a for loop.

    :return: Deck of cards
    """
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    """Function creates a deck of cards with
    a list comprehension.

    :return: Deck of cards
    """
    deck = [(s, v) for s in SUITS for v in VALUES]
    return deck
