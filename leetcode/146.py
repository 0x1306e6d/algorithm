"""
    File: 146.py
    Title: LRU Cache
    Difficulty: Medium
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.pointer = {}

    def get(self, key: int) -> int:
        if key not in self.pointer:
            return -1
        node = self._remove(key)
        return self._add(key, node.value).value

    def put(self, key: int, value: int) -> None:
        if key in self.pointer:
            self._remove(key)
        node = self._add(key, value)
        if len(self.pointer) > self.capacity:
            self._remove(self.head.next.key)

    def _add(self, key, value):
        node = Node(key, value)
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.pointer[key] = node
        return node

    def _remove(self, key):
        node = self.pointer[key]
        del self.pointer[key]
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
