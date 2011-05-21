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
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    node = stack.pop()
    print node.minimum
    stack.push(0)
    stack.push(4)
    node = stack.pop()
    print node.min()
    print stack.min()
    print stack

if __name__ == '__main__':
    main()
