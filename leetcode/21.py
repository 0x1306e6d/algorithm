"""
    File: 21.py
    Title: Merge Two Sorted Lists
    Difficulty: Easy
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        root = ListNode(None)
        current = root
        n1, n2 = list1, list2
        while n1 or n2:
            if n1 is None:
                current.next = n2
                return root.next
            if n2 is None:
                current.next = n1
                return root.next
            if n1.val > n2.val:
                current.next = n2
                current = current.next
                n2 = n2.next
            else:
                current.next = n1
                current = current.next
                n1 = n1.next
        return root.next
