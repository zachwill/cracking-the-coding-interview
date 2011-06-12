#!/usr/bin/env python

"""
You have a string and need to find the first non-repeating characters in the
string.

For earlier versions of Python, the OrderedDict data structure is available
from the Python cookbook: http://code.activestate.com/recipes/576693/

NOTE: This approach goes through the string twice, but is still O(N).
"""

from collections import OrderedDict, deque


def iterable_to_ordered_dict(iterable):
    """
    Change from an iterable data structure (list, tuple, string) to an
    ordered dictionary data structure.
    """
    ordered_dict = OrderedDict()
    for letter in iterable:
        if letter in ordered_dict and ordered_dict[letter] == 1:
            # No real need to += increment the value,
            # it no longer meets our requirements.
            ordered_dict[letter] = False
        else:
            ordered_dict[letter] = 1
    return ordered_dict


def find_first_value(ordered_dict):
    """Find first non-repeating character."""
    for letter in ordered_dict.keys():
        if ordered_dict[letter] == 1:
            return letter
    return False


def first_value_queue(ordered_dict):
    """
    Return a queue of values that can then be popped to return the next
    occurence of a non-repeating character in a string.
    """
    queue = deque(letter for letter in ordered_dict.keys() if
                  ordered_dict[letter])
    return queue


def main():
    d = iterable_to_ordered_dict('abacaddeea')
    print find_first_value(d)  # b
    queue = first_value_queue(d)
    print queue.popleft()      # b
    print queue.popleft()      # c


if __name__ == '__main__':
    main()
