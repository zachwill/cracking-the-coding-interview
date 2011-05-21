#!/usr/bin/env python


def reverse(string):
    """Reverse a given string."""
    return string[::-1]

if __name__ == '__main__':
    print reverse('a')
    print reverse('abcd')
    print reverse('hello world')
