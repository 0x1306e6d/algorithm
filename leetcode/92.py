"""
    File: 92.py
    Title: Reverse Linked List II
    Difficulty: Medium
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int,
    ) -> Optional[ListNode]:
        idx = 1
        left_node_before, left_node = None, head
        while idx < left:
            idx += 1
            left_node_before = left_node
            left_node = left_node.next

        prev, current = None, left_node
        count = right - left + 1
        while count:
            next = current.next
            current.next = prev
            prev, current = current, next
            count -= 1
        left_node.next = current
        if left_node_before:
            left_node_before.next = prev
            return head
        else:
            return prev
