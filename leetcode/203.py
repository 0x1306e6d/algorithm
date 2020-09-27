"""
    File: 203.py
    Title: Remove Linked List Elements
    Difficulty: Easy
    URL: https://leetcode.com/problems/remove-linked-list-elements/
"""

import unittest

from typing import List


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

    def __eq__(self, o):
        return (self.val == o.val) and (self.next == o.next)

    def __repr__(self):
        if self.next is None:
            return "{}".format(self.val)
        else:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None

        removed = ListNode()
        removed_node = removed
        node = head
        while node is not None:
            if node.val != val:
                removed_node.next = ListNode(node.val)
                removed_node = removed_node.next
            node = node.next

        return removed.next


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(
            4, ListNode(5, ListNode(6)))))))
        val = 6
        # Output
        output = ListNode(1, ListNode(2, ListNode(3, ListNode(
            4, ListNode(5)))))

        solution = Solution()
        self.assertEqual(solution.removeElements(head, val), output)


if __name__ == "__main__":
    unittest.main()
