"""
    File: 143.py
    Title: Reorder List
    Difficulty: Medium
    URL: https://leetcode.com/problems/reorder-list/
"""

import unittest

from typing import Optional


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
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        class DoubleListNode:
            def __init__(self,
                         delegate: ListNode,
                         previous: "DoubleListNode" = None,
                         next: "DoubleListNode" = None):
                self.delegate = delegate
                self.val = delegate.val
                self.previous = previous
                self.next = next
                self.reordered = False

            def __eq__(self, o):
                if o is None:
                    return False
                return (self.val == o.val) \
                    and (self.previous == o.previous) \
                    and (self.next == o.next)

            def __repr__(self):
                if self.next is None:
                    return "{} -> None".format(self.val)
                else:
                    return "{} -> {}".format(self.val, self.next)

        double_head = DoubleListNode(head)
        double_head.reordered = True
        double_tail = double_head

        current = head
        double_current = double_head
        while current.next:
            double_node = DoubleListNode(current.next, double_current)
            double_current.next = double_node
            double_current = double_node
            double_tail = double_current
            current = current.next

        current = head
        right = double_head.next
        left = double_tail
        while True:
            reordered = False
            if (left is not None) and (left.reordered == False):
                current.next = left.delegate
                current = current.next
                current.next = None

                left.reordered = True
                left = left.previous

                reordered = True

            if (right is not None) and (right.reordered == False):
                current.next = right.delegate
                current = current.next
                current.next = None

                right.reordered = True
                right = right.next

                reordered = True

            if reordered == False:
                break


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        # Output
        output = ListNode(1, ListNode(4, ListNode(2, ListNode(3))))

        solution = Solution()
        solution.reorderList(head)
        self.assertEqual(head, output)

    def test_example2(self):
        # Input
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        # Output
        output = ListNode(1,
                          ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))

        solution = Solution()
        solution.reorderList(head)
        self.assertEqual(head, output)


if __name__ == "__main__":
    unittest.main()
