#!/usr/bin/env python

"""
Design the data structure for a generic deck of cards.

Python Docs:  http://docs.python.org/reference/datamodel.html
"""


class Card(object):

    def __init__(self, card_value, suit=None, game_value=None):
        face_cards = {'J': 11, 'Q': 12,
                      'K': 13, 'A': 1}
        if game_value:
            self.game_value = game_value
        elif card_value in face_cards:
            self.game_value = face_cards[card_value]
        else:
            self.game_value = card_value
        self.card_value = str(card_value)
        self.suit = suit

    def __repr__(self):
        if self.suit:
            return ' '.join(['[', self.card_value, 'of', self.suit, ']'])
        return ' '.join(['[', self.card_value, ']'])

    def __cmp__(self, other):
        """Called by comparison operators."""
        return self.game_value - other.game_value


def main():
    jack = Card('J', 'clubs')
    print jack

    king = Card('K', 'hearts')
    print king
    print 'K > J:', king > jack

    ten = Card(10, 'diamonds')
    print ten
    print '10 < J:', ten < jack

    queen = Card('Q', 'spades')
    print queen
    print 'J < Q < K:', jack < queen < king

    joker = Card('Joker', game_value=100)
    print joker
    print 'Joker > K:', joker > king


if __name__ == '__main__':
    main()
