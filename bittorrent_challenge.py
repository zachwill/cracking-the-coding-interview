#!/usr/bin/env python

"""
My solution to the BitTorrent Developer Challenge -- takes forever to run.

You have 40 bowls, all placed in a line at exact intervals of 1 meter. You
also have 9 oranges. You wish to place all the oranges in the bowls, no
more than one orange in each bowl, so that there are no three oranges A, B,
and C such that the distance between A and B is equal to the distance
between B and C. How many ways can you arrange the oranges in the bowls?.
"""

from itertools import combinations, imap


def eliminate(combo):
    """Eliminate combinations that do not fit the criteria."""
    for a, b, c in combo:
        if abs(a - b) == abs(b - c):
            return False
    return True


def main():
    combos = (combinations(c, 3) for c in combinations(xrange(40), 9))
    print sum(imap(eliminate, combos))  # 7,555,794

if __name__ == '__main__':
    main()
