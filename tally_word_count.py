#!/usr/bin/env python

"""
Tally the length of words in the `word_list.txt` file.

The Counter datatype became available in Python 2.7 and greater.

Python 2.5 Counter:  http://code.activestate.com/recipes/576611/
"""

from collections import Counter


def main():
    with open('files/word_list.txt') as f:
        # Create a generator of word length.
        words = (len(word.strip()) for word in f)
        counter = Counter(words)
    for count, length in counter.items():
        if len(str(count)) == 2:
            print "%d : %d" % (count, length)
        else:
            print "%d  : %d" % (count, length)


if __name__ == '__main__':
    main()
