"""
    File: 155.py
    Title: Min Stack
    Difficulty: Medium
"""

inf = float("inf")


def heappush(h, x):
    h.append(x)
    pos = len(h) - 1
    while pos > 0:
        parent = (pos - 1) // 2
        if h[pos] < h[parent]:
            h[pos], h[parent] = h[parent], h[pos]
            pos = parent
        else:
            break


def heapremove(h, x):
    for i in range(len(h)):
        if h[i] == x:
            break
    h[i] = -inf
    heapup(h, i)
    heappop(h)


def heapup(h, idx):
    pos = idx
    while pos > 0:
        parent = (pos - 1) // 2
        if h[pos] < h[parent]:
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
            if right < len(h) and h[child] > h[right]:
                child = right
            if h[pos] > h[child]:
                h[pos], h[child] = h[child], h[pos]
                pos = child
                child = 2 * pos + 1
            else:
                break
        return first
    return last


class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heappush(self.heap, val)

    def pop(self) -> None:
        x = self.stack.pop()
        heapremove(self.heap, x)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.heap[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
