"""
    File: 1474.py
    Title: Delete N Nodes After M Nodes of a Linked List
    Difficulty: Easy
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        node = head
        while node:
            for i in range(m - 1):
                if not node:
                    break
                node = node.next
            if not node:
                break

            tail = node
            node = node.next
            tail.next = None

            for i in range(n):
                if not node:
                    break
                node = node.next
            if not node:
                break

            tail.next = node
        return head
