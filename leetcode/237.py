"""
    File: 237.py
    Title: Delete Node in a Linked List
    Difficulty: Medium
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current, next = node, node.next
        while True:
            current.val = next.val

            if next.next is None:
                current.next = None
                break
            else:
                current = next
                next = next.next
