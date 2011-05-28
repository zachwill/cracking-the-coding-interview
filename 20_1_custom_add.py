#!/usr/bin/env python

"""
Write a function that adds two numbers -- but no arithmetic operators can be
used.
"""

def sum_add(first, second):
    """Kind of cheating to use Python's sum function."""
    return sum([first, second])


def binary_add(first, second):
    """Binary voodoo magic."""
    if second == 0:
        return first
    elif first == 0:
        return second
    xor = first ^ second
    carry = (first & second) << 1
    return binary_add(xor, carry)


def array_add(first, second):
    """
    Addition with bytearrays. Since arrays allocate a specific amount of
    memory, this way is somewhat inefficient -- but about twice as fast as
    using Python's range function.
    """
    first_array = bytearray(first)
    second_array = bytearray(second)
    first_array.extend(second_array)
    return len(first_array)


def main():
    # Sum way.
    print sum_add(0, 1)       # 1
    print sum_add(2, 3)       # 5
    print sum_add(20, 12)     # 32
    print sum_add(50, 49)     # 99
    # Binary way.
    print binary_add(0, 1)    # 1
    print binary_add(2, 3)    # 5
    print binary_add(20, 12)  # 32
    print binary_add(50, 49)  # 99
    # With bytearrays.
    print array_add(0, 1)     # 1
    print array_add(2, 3)     # 5
    print array_add(20, 12)   # 32
    print array_add(50, 49)   # 99


if __name__ == '__main__':
    main()
