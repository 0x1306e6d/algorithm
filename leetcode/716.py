"""
    File: 716.py
    Title: Max Stack
    Difficulty: Hard
"""

from collections import defaultdict


def heappush(h, x):
    h.append(x)
    pos = len(h) - 1
    while pos > 0:
        parent = (pos - 1) // 2
        if h[pos] > h[parent]:
            h[pos], h[parent] = h[parent], h[pos]
            pos = parent
        else:
            break


def heappop(h):
    last = h.pop()
    if h:
        first = h[0]
        h[0] = last
        pos, child = 0, 1
        while child < len(h):
            right = child + 1
            if right < len(h) and h[right] > h[child]:
                child = right
            if h[pos] < h[child]:
                h[pos], h[child] = h[child], h[pos]
                pos = child
                child = 2 * pos + 1
            else:
                break
        return first
    return last


def heapremove(h, x):
    idx = 0
    for idx in range(len(h)):
        if h[idx] == x:
            break
    h[idx] = float("inf")
    pos = idx
    while pos > 0:
        parent = (pos - 1) // 2
        h[pos], h[parent] = h[parent], h[pos]
        pos = parent
    heappop(h)


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MaxStack:

    def __init__(self):
        self.tail = None
        self.nodes = defaultdict(list)
        self.h = []

    def push(self, x: int) -> None:
        node = Node(x, self.tail)
        if self.tail:
            self.tail.next = node
        self.tail = node
        self.nodes[x].append(node)
        heappush(self.h, x)

    def pop(self) -> int:
        node = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.nodes[node.val].pop()
        heapremove(self.h, node.val)
        return node.val

    def top(self) -> int:
        return self.tail.val

    def peekMax(self) -> int:
        return self.h[0]

    def popMax(self) -> int:
        maximum = heappop(self.h)
        node = self.nodes[maximum].pop()
        if self.tail.val == node.val:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            prev, next = node.prev, node.next
            if prev:
                prev.next = next
            if next:
                next.prev = prev
        return maximum


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
