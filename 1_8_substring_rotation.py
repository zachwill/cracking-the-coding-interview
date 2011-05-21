#!/usr/bin/env python


def is_rotation(first, second):
    """Given two strings, is one a rotation of the other."""
    if len(first) is not len(second):
        return False
    double_second = second + second
    return first in double_second

if __name__ == '__main__':
    print is_rotation('apple', 'pleap')  # True
    print is_rotation('apple', 'ppale')  # False
    print is_rotation('zach', 'chza')    # True
