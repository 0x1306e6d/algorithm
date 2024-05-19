"""
    File: 642.py
    Title: Design Search Autocomplete System
    Difficulty: Hard
"""

from typing import List


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        for sentence, time in zip(sentences, times):
            self._add(sentence, time)
        self.query = ""

    def input(self, c: str) -> List[str]:
        if c == "#":
            self._add(self.query, 1)
            self.query = ""
            return []

        self.query += c

        node = self._find()
        if node is None:
            return []

        arr = []
        self._populate(node, self.query, arr)
        arr.sort()

        ans = []
        for i in range(min(3, len(arr))):
            ans.append(arr[i][1])
        return ans

    def _add(self, sentence, time):
        node = self.trie
        for c in sentence:
            if c not in node:
                node[c] = {}
            node = node[c]
        if 0 in node:
            node[0] += time
        else:
            node[0] = time

    def _find(self):
        node = self.trie
        for c in self.query:
            if c in node:
                node = node[c]
            else:
                return None
        return node

    def _populate(self, node, prefix, arr):
        for c in node:
            if c == 0:
                arr.append((-node[0], prefix))
            else:
                self._populate(node[c], prefix + c, arr)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
