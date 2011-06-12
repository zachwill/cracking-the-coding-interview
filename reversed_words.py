#!/usr/bin/env python

"""
Reverse the word order for the words in a sentence.

Example:
    I like to write Python.

Becomes:
    Python. write to like I
"""


def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))


def main():
    sentence = "I like to write Python."
    print reverse_words(sentence)


if __name__ == '__main__':
    main()
