#!/usr/bin/env python

"""
SetOfStacks should be composed of several stacks, and should create a new
stack one the previous one exceeds capacity. SetOfStacks push and pop methods
should behave identically to a single stack.
"""

class SetOfStacks(list):

    def __init__(self, capacity=4):
        self.stacks = []
        self.last_stack = []
        self.capacity = capacity
        self.stacks.append(self.last_stack)

    def __repr__(self):
        return str(self.stacks)

    def push(self, number):
        last_stack = self.last_stack
        if len(last_stack) is self.capacity:
            last_stack = []
            self.last_stack = last_stack
            self.stacks.append(last_stack)
        last_stack.append(number)

    def pop(self):
        last_stack = self.last_stack
        number = last_stack.pop()
        if len(last_stack) is 0:
            self.stacks.pop()
            self.last_stack = self.stacks[-1]
        return number


def main():
    stack = SetOfStacks()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print stack
    stack.pop()
    stack.pop()
    stack.pop()
    print stack

if __name__ == '__main__':
    main()
