"""
    File: 82.py
    Title: Remove Duplicates from Sorted List II
    Difficulty: Medium
    URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""

import unittest

from typing import List


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

    def __eq__(self, o) -> bool:
        if o is None:
            return False
        return (self.val == o.val) and (self.next == o.next)

    def __repr__(self):
        if self.next is None:
            return "{}".format(self.val)
        else:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        distinct_head = None
        distinct_current = None

        current = head
        overwrite = False
        while current:
            if distinct_current is None:
                distinct_head = ListNode(current.val)
                distinct_current = distinct_head
            else:
                if distinct_current.val == current.val:
                    overwrite = True
                else:
                    if overwrite:
                        distinct_current.val = current.val
                    else:
                        distinct_current.next = ListNode(current.val)
                        distinct_current = distinct_current.next
                    overwrite = False
            current = current.next
        if overwrite:
            if distinct_head.next is None:
                distinct_head = None
            else:
                current = distinct_head
                while current.next and current.next.val != distinct_current.val:
                    current = current.next
                current.next = None

        return distinct_head


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        head = self.make_head([1, 2, 3, 3, 4, 4, 5])
        # Output
        output = self.make_head([1, 2, 5])

        solution = Solution()
        self.assertEqual(solution.deleteDuplicates(head), output)

    def test_example2(self):
        # Input
        head = self.make_head([1, 1, 1, 2, 3])
        # Output
        output = self.make_head([2, 3])

        solution = Solution()
        self.assertEqual(solution.deleteDuplicates(head), output)

    def make_head(self, nodes: List[int]) -> ListNode:
        head = None
        current = None
        for node in nodes:
            if head is None:
                head = ListNode(node)
                current = head
            else:
                current.next = ListNode(node)
                current = current.next
        return head


if __name__ == "__main__":
    unittest.main()
