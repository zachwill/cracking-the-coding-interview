#!/usr/bin/env python


def anagram(first, second):
    """Decide if two strings are anagrams of one another."""
    return sorted(first) == sorted(second)


def main():
    print anagram('a', 'b')
    print anagram('a', 'aa')
    print anagram('hi', 'hi')
    print anagram('hello there', 'there hello')

if __name__ == '__main__':
    main()
