#!/usr/bin/env python

import re


def replace_space(string):
    """Replace all spaces in a word with `%20`."""
    return re.sub(' ', '%20', string)


def main():
    print replace_space('abcd')
    print replace_space('hello world')
    print replace_space('another working example')

if __name__ == '__main__':
    main()
