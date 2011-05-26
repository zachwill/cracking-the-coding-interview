#!/usr/bin/env python

"""
Towers of Hanoi in Python.

Originally from:  http://codesnippets.joyent.com/posts/show/530

Notice how it takes 2^n - 1 number of moves to complete.
To see this for yourself, run the following from the commandline:
    python 3_4_hanoi.py | wc -l
"""


def hanoi(n, a='A', b='B', c='C'):
    """Move n discs from a to c using b as middle."""
    if n == 0:
        return
    hanoi(n - 1, a, c, b)
    print a, '->', c
    hanoi(n - 1, b, a, c)


def main():
    hanoi(4)


if __name__ == '__main__':
    main()
