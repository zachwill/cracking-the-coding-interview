#!/usr/bin/env python

"""
Write a program to sort a stack.

This is O(N^2).
"""


def built_in_sort(stack):
    stack.sort()
    return stack


def custom_sort(stack):
    """Custom version of list sort. This should never be used."""
    new_stack = []
    while len(stack):
        temp = stack.pop()
        while len(new_stack) and new_stack[-1] > temp:
            stack.append(new_stack.pop())
        new_stack.append(temp)
    return new_stack


def main():
    stack = [1, 3, 2, 4, 6, 5]
    print built_in_sort(stack)
    print custom_sort(stack)


if __name__ == '__main__':
    main()
