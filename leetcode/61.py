"""
    File: 61.py
    Title: Rotate List
    Difficulty: Medium
    URL: https://leetcode.com/problems/rotate-list/
"""

import unittest

from typing import List


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

    def __eq__(self, o):
        if o is None:
            return False
        return (self.val == o.val) and (self.next == o.next)

    def __repr__(self):
        if self.next is None:
            return "{} -> None".format(self.val)
        else:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head

        tail = head
        length = 1
        while tail.next is not None:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        new_head = head
        new_tail = None
        for i in range(length - k):
            new_tail = new_head
            new_head = new_head.next if new_head.next is not None else head
        new_head_tail = new_head
        while new_head_tail.next is not None:
            new_head_tail = new_head_tail.next
        new_head_tail.next = head
        new_tail.next = None
        return new_head


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        k = 2
        # Output
        output = ListNode(4, ListNode(5, ListNode(1, ListNode(2,
                                                              ListNode(3)))))

        solution = Solution()
        self.assertEqual(solution.rotateRight(head, k), output)

    def test_example2(self):
        # Input
        head = ListNode(0, ListNode(1, ListNode(2)))
        k = 4
        # Output
        output = ListNode(2, ListNode(0, ListNode(1)))

        solution = Solution()
        self.assertEqual(solution.rotateRight(head, k), output)


if __name__ == "__main__":
    unittest.main()
