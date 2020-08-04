"""
    File: 677.py
    Title: Map Sum Pairs
    Difficulty: Medium
    URL: https://leetcode.com/problems/map-sum-pairs/
"""

import queue
import unittest


class MapSum:
    def __init__(self):
        self.tree = {}

    def insert(self, key: str, val: int) -> None:
        node = self.tree
        for k in key:
            if k not in node:
                node[k] = {}
            node = node[k]
        node['value'] = val

    def sum(self, prefix: str) -> int:
        node = self.tree
        for c in prefix:
            if c in node:
                node = node[c]
            else:
                print(self.tree)
                return 0

        ret = 0
        q = queue.deque()
        q.append(node)
        while q:
            p = q.popleft()
            for k in p:
                if k == 'value':
                    ret += p['value']
                else:
                    q.append(p[k])
        return ret


class MapSumTestCase(unittest.TestCase):
    def test_example1(self):
        obj = MapSum()

        self.assertEqual(obj.insert("apple", 3), None)
        self.assertEqual(obj.sum("ap"), 3)
        self.assertEqual(obj.insert("app", 2), None)
        self.assertEqual(obj.sum("ap"), 5)


if __name__ == "__main__":
    unittest.main()
