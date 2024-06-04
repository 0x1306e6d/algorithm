"""
    File: 234.py
    Title: Palindrome Linked List
    Difficulty: Easy
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, current = slow, slow.next
        prev.next = None
        while current:
            next = current.next
            current.next = prev
            prev, current = current, next

        forward, backward = head, prev
        while forward and backward:
            if forward.val != backward.val:
                return False
            forward = forward.next
            backward = backward.next
        return True
