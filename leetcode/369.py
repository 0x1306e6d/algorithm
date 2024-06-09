"""
    File: 369.py
    Title: Plus One Linked List
    Difficulty: Medium
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)

        start = dummy
        node = head
        while node:
            if node.val != 9:
                start = node
            node = node.next

        start.val += 1
        node = start.next
        while node:
            node.val = 0
            node = node.next

        if dummy.val == 0:
            return dummy.next
        return dummy
