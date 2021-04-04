"""
    File: 328.py
    Title: Odd Even Linked List
    Difficulty: Medium
    URL: https://leetcode.com/problems/odd-even-linked-list/
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        odd_head = None
        odd_current = None
        even_head = None
        even_curent = None

        index = 1
        current = head
        while current:
            if index % 2 == 0:
                if even_curent is None:
                    even_head = ListNode(current.val)
                    even_curent = even_head
                else:
                    even_curent.next = ListNode(current.val)
                    even_curent = even_curent.next
            else:
                if odd_current is None:
                    odd_head = ListNode(current.val)
                    odd_current = odd_head
                else:
                    odd_current.next = ListNode(current.val)
                    odd_current = odd_current.next

            index += 1
            current = current.next
        odd_current.next = even_head
        return odd_head


class solutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        head = self.make_head([1, 2, 3, 4, 5])
        # Output
        output = self.make_head([1, 3, 5, 2, 4])

        solution = Solution()
        self.assertEqual(solution.oddEvenList(head), output)

    def test_example2(self):
        # Input
        head = self.make_head([2, 1, 3, 5, 6, 4, 7])
        # Output
        output = self.make_head([2, 3, 6, 7, 1, 5, 4])

        solution = Solution()
        self.assertEqual(solution.oddEvenList(head), output)

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
