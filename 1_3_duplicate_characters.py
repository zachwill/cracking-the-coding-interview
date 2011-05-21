#!/usr/bin/env python


def remove_duplicates(string):
    """Remove duplicate characters in a string."""
    return set(string)


def remove_with_dict(string):
    """Implement my own set function."""
    string_dict = {}
    for letter in string:
        string_dict[letter] = True
    return string_dict.keys()

if __name__ == '__main__':
    print remove_duplicates('a')
    print remove_duplicates('abcd')
    print remove_duplicates('abcda')
    print remove_with_dict('a')
    print remove_with_dict('abcd')
    print remove_with_dict('abcda')
