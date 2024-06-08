"""
    File: 1506.py
    Title: Find Root of N-Ary Tree
    Difficulty: Medium
"""

from collections import defaultdict
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List["Node"]) -> "Node":
        nodes = {}
        indegree = defaultdict(int)
        for node in tree:
            if node.val not in indegree:
                indegree[node.val] = 0
            nodes[node.val] = node
            for child in node.children:
                indegree[child.val] += 1
        for val in indegree:
            if indegree[val] == 0:
                return nodes[val]
