"""
    File: 1429.py
    Title: First Unique Number
    Difficulty: Medium
"""

from collections import defaultdict
from typing import List


class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.counts = defaultdict(int)
        for num in nums:
            self.counts[num] += 1
        self.head = None
        self.tail = None
        self.nums = {}
        for num in self.counts:
            if self.counts[num] == 1:
                self._add(num)

    def _add(self, num):
        node = Node(val=num, prev=self.tail, next=None)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.nums[num] = node

    def _remove(self, num):
        node = self.nums[num]
        prev, next = node.prev, node.next
        if prev is not None:
            prev.next = next
        if next is not None:
            next.prev = prev
        if node == self.head:
            self.head = next
        if node == self.tail:
            self.tail = prev

    def showFirstUnique(self) -> int:
        if self.head is None:
            return -1
        return self.head.val

    def add(self, value: int) -> None:
        self.counts[value] += 1
        if self.counts[value] == 1:
            self._add(value)
        elif self.counts[value] == 2:
            self._remove(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
