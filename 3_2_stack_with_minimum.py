#!/usr/bin/env python

"""
Design a stack, which in addition to push and pop, also has a function to
return the minimum element.
"""

class Stack(list):

    def push(self, number):
        """Push method -- similar to other languages."""
        if len(self) > 0:
            last = self[-1]
            minimum = self._find_minimum(number, last)
        else:
            minimum = number
        self.minimum = minimum
        self.append(NodeWithMin(number, minimum))

    def _find_minimum(self, number, last_number):
        """Internal method to compare two numbers."""
        if number < last_number.minimum:
           return number
        return last_number.minimum

    def min(self):
        """Return the minimum element."""
        return self.minimum


class NodeWithMin(object):

    def __init__(self, number, minimum):
        self.number = number
        self.minimum = minimum

    def __repr__(self):
        return str(self.number)

    def min(self):
        return self.minimum


def main():
    z = Stack()
    z.push(1)
    z.push(2)
    z.push(3)
    node = z.pop()
    print node.minimum
    z.push(0)
    z.push(4)
    node = z.pop()
    print node.min()
    print z.min()
    print z

if __name__ == '__main__':
    main()
