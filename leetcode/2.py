"""
    File: 2.py
    Title: Add Two Numbers
    Difficulty: Medium
    URL: https://leetcode.com/problems/add-two-numbers/
"""

import unittest


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

    def __eq__(self, o):
        return (self.val == o.val) and (self.next == o.next)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1.val
        n2 = l2.val

        d = 10
        ll1 = l1.next
        ll2 = l2.next
        while (ll1 is not None) or (ll2 is not None):
            if (ll1 is not None):
                n1 += (ll1.val * d)
                ll1 = ll1.next
            if (ll2 is not None):
                n2 += (ll2.val * d)
                ll2 = ll2.next
            d *= 10

        n = n1 + n2
        if n == 0:
            return ListNode(0)

        root = None
        current = None
        while n > 0:
            if root is None:
                root = ListNode(n % 10)
            else:
                if current is None:
                    current = ListNode(n % 10)
                    root.next = current
                else:
                    current.next = ListNode(n % 10)
                    current = current.next
            n //= 10
        return root


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        # Output
        output = ListNode(7, ListNode(0, ListNode(8)))

        solution = Solution()
        self.assertEqual(solution.addTwoNumbers(l1, l2), output)


if __name__ == "__main__":
    unittest.main()
