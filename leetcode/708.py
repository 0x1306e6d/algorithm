"""
    File: 708.py
    Title: Insert into a Sorted Circular Linked List
    Difficulty: Medium
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node

        prev, curr = head, head.next
        while True:
            insert = False
            if prev.val <= insertVal <= curr.val:
                insert = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    insert = True

            if insert:
                node = Node(insertVal)
                prev.next = node
                node.next = curr
                return head

            prev, curr = curr, curr.next
            if prev == head:
                break

        node = Node(insertVal)
        prev.next = node
        node.next = curr
        return head
