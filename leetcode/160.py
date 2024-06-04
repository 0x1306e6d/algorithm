"""
    File: 160.py
    Title: Intersection of Two Linked Lists
    Difficulty: Easy
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode,
    ) -> Optional[ListNode]:
        lenA = 1
        endA = headA
        while endA.next:
            lenA += 1
            endA = endA.next

        lenB = 1
        endB = headB
        while endB.next:
            lenB += 1
            endB = endB.next

        if endA != endB:
            return None

        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        elif lenB > lenA:
            for _ in range(lenB - lenA):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
