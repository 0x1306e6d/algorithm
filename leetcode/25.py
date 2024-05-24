"""
    File: 25.py
    Title: Reverse Nodes in k-Group
    Difficulty: Hard
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            check = node
            for _ in range(k):
                if check:
                    check = check.next
                else:
                    return node

            first, prev, current = node, None, node
            for _ in range(k):
                next = current.next
                current.next = prev
                prev, current = current, next
            root = prev
            first.next = reverse(current)
            return root

        return reverse(head)
