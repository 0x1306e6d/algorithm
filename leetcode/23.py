"""
    File: 23.py
    Title: Merge k Sorted Lists
    Difficulty: Hard
"""

from heapq import heappush, heappop
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Holder:
    def __init__(self, val, node):
        self.val = val
        self.node = node

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode(None)
        current = root

        h = []
        for l in lists:
            if l is None:
                continue
            heappush(h, Holder(l.val, l))
        while h:
            holder = heappop(h)
            val, node = holder.val, holder.node
            current.next = ListNode(val)
            current = current.next

            if node.next:
                heappush(h, Holder(node.next.val, node.next))
        return root.next
