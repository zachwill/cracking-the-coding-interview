#!/usr/bin/env python

"""
Write a function that adds two numbers -- but no arithmetic operators can be
used.
"""


def custom_add(first, second):
    """Binary voodoo magic."""
    if second is 0:
        return first
    elif first is 0:
        return second
    combine = first ^ second
    carry = (first & second) << 1
    return custom_add(combine, carry)


def main():
    print custom_add(0, 1)    # 1
    print custom_add(2, 3)    # 5
    print custom_add(20, 12)  # 32
    print custom_add(50, 49)  # 99

if __name__ == '__main__':
    main()
