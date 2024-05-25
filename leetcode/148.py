"""
    File: 148.py
    Title: Sort List
    Difficulty: Medium
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        a, b = head, slow.next
        if b is None:  # 2
            if head.val < slow.val:
                return head
            else:
                slow.next = head
                head.next = None
                return slow

        slow.next = None
        a, b = self.sortList(a), self.sortList(b)
        dummy = ListNode(0)
        node = dummy
        while a or b:
            if a is None:
                node.next = b
                break
            if b is None:
                node.next = a
                break
            if a.val < b.val:
                node.next = a
                node = node.next
                a = a.next
            else:
                node.next = b
                node = node.next
                b = b.next
        return dummy.next
