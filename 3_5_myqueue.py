#!/usr/bin/env python

"""
Implement a queue with two stacks in the MyQueue class.

This should never be used, though -- the deque data structure from the
standard library collections module should be used instead.
"""


class MyQueue(object):

    def __init__(self):
        self.first = []
        self.second = []

    def size(self):
        return len(self.first) + len(self.second)

    def add(self, number):
        self.first.append(number)

    def peek(self):
        first = self.first
        second = self.second
        if len(second):
            return second[-1]
        while len(first):
            second.append(first.pop())
        return second[-1]

    def remove(self):
        first = self.first
        second = self.second
        if len(second):
            return second.pop()
        while len(first):
            second.append(first.pop())
        return second.pop()


def main():
    queue = MyQueue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    print queue.size()    # 3
    print queue.peek()    # 1
    print queue.remove()  # 1
    print queue.peek()    # 2

if __name__ == '__main__':
    main()
