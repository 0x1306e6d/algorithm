"""
    File: 225.py
    Title: Implement Stack using Queues
    Difficulty: Easy
    URL: https://leetcode.com/problems/implement-stack-using-queues/
"""

import unittest

from collections import deque


class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        if len(self.queue1) == 0:
            src = self.queue2
            dst = self.queue1
        else:
            src = self.queue1
            dst = self.queue2

        dst.append(x)
        while src:
            dst.append(src.popleft())

    def pop(self) -> int:
        if len(self.queue1) == 0:
            return self.queue2.popleft()
        else:
            return self.queue1.popleft()

    def top(self) -> int:
        if len(self.queue1) == 0:
            return self.queue2[0]
        else:
            return self.queue1[0]

    def empty(self) -> bool:
        if len(self.queue1) == 0:
            return len(self.queue2) == 0
        else:
            return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.empty(), False)


if __name__ == "__main__":
    unittest.main()
