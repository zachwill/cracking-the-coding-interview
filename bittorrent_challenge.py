#!/usr/bin/env python

"""
My solution to the BitTorrent Developer Challenge.

You have 40 bowls, all placed in a line at exact intervals of 1 meter. You
also have 9 oranges. You wish to place all the oranges in the bowls, no
more than one orange in each bowl, so that there are no three oranges A, B,
and C such that the distance between A and B is equal to the distance
between B and C. How many ways can you arrange the oranges in the bowls?.
"""

from itertools import combinations


def eliminate_combos(combination):
    """
    Eliminate combinations that do not meet the following the requirement:
    the absolute difference between the current value and the previous value
    must not be the same as the current value and the next value in the
    combination.
    """
    last_item = len(combination) - 1
    for index, value in enumerate(combination):
        if index is last_item:
            # Successfully iterated through all elements.
            return True
        elif index is not 0:
            last_val = combination[index - 1]
            next_val = combination[index + 1]
            if abs(value - last_val) is abs(next_val - value):
                return False
        else:
            # Very first element of combination.
            continue


def main():
    combos = (c for c in combinations(xrange(40), 9) if eliminate_combos(c))
    print sum(1 for combo in combos)  # 105,993,066

if __name__ == '__main__':
    main()
