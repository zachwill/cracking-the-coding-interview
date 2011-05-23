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
    xor = first ^ second
    carry = (first & second) << 1
    return custom_add(xor, carry)


def array_add(first, second):
    """Addition with bytearrays."""
    first_array = bytearray(first)
    second_array = bytearray(second)
    first_array.extend(second_array)
    return len(first_array)


def main():
    # Binary way.
    print custom_add(0, 1)    # 1
    print custom_add(2, 3)    # 5
    print custom_add(20, 12)  # 32
    print custom_add(50, 49)  # 99
    # With bytearrays.
    print array_add(0, 1)    # 1
    print array_add(2, 3)    # 5
    print array_add(20, 12)  # 32
    print array_add(50, 49)  # 99

if __name__ == '__main__':
    main()
