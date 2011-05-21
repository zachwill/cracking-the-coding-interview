#!/usr/bin/env python


def anagram(first, second):
    """Decide if two strings are anagrams of one another."""
    return sorted(first) == sorted(second)

if __name__ == '__main__':
    print anagram('a', 'b')
    print anagram('a', 'A')
    print anagram('hi', 'hi')
    print anagram('hello there', 'hello there')
