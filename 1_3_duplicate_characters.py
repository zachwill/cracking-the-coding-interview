#!/usr/bin/env python


def remove_duplicates(string):
    """Remove duplicate characters in a string."""
    return set(string)


def remove_with_dict(string):
    """Implement own set function as dict keys."""
    string_dict = {}
    for letter in string:
        if letter not in string_dict:
            string_dict[letter] = True
    return string_dict.keys()


def main():
    # Sets.
    print remove_duplicates('a')
    print remove_duplicates('abb')
    print remove_duplicates('abcd')
    print remove_duplicates('abcda')
    # List of dictionay keys.
    print remove_with_dict('a')
    print remove_with_dict('abb')
    print remove_with_dict('abcd')
    print remove_with_dict('abcda')

if __name__ == '__main__':
    main()
