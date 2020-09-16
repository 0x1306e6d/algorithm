"""
    File: 641.py
    Title: Design Circular Deque
    Difficulty: Medium
    URL: https://leetcode.com/problems/design-circular-deque/
"""

import unittest

from typing import List


class Item:
    def __init__(self, value: int):
        self.value = value
        self.top = None
        self.bottom = None


class MyCircularDeque:
    def __init__(self, k: int):
        self._capacity = k
        self._size = 0
        self._top = None
        self._bottom = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        item = Item(value)
        if self.isEmpty():
            self._top = item
            self._bottom = item
        else:
            item.bottom = self._top
            self._top.top = item
            self._top = item
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        item = Item(value)
        if self.isEmpty():
            self._top = item
            self._bottom = item
        else:
            item.top = self._bottom
            self._bottom.bottom = item
            self._bottom = item
        self._size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        top = self._top
        self._top = top.bottom
        if self._top is not None:
            self._top.top = None
        self._size -= 1

        if self.isEmpty():
            self._top = None
            self._bottom = None

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        bottom = self._bottom
        self._bottom = bottom.top
        if self._bottom is not None:
            self._bottom.bottom = None
        self._size -= 1

        if self.isEmpty():
            self._top = None
            self._bottom = None

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self._top.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self._bottom.value

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._capacity


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        circular_deque = MyCircularDeque(3)
        self.assertEqual(circular_deque.insertLast(1), True)
        self.assertEqual(circular_deque.insertLast(2), True)
        self.assertEqual(circular_deque.insertFront(3), True)
        self.assertEqual(circular_deque.insertFront(4), False)
        self.assertEqual(circular_deque.getRear(), 2)
        self.assertEqual(circular_deque.isFull(), True)
        self.assertEqual(circular_deque.deleteLast(), True)
        self.assertEqual(circular_deque.insertFront(4), True)
        self.assertEqual(circular_deque.getFront(), 4)


if __name__ == "__main__":
    unittest.main()
