#!/usr/bin/env python


def reverse(string):
    """Reverse a given string."""
    return string[::-1]


def main():
    print reverse('a')
    print reverse('abcd')
    print reverse('hello world')

if __name__ == '__main__':
    main()
