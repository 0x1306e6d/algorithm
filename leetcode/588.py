"""
    File: 588.py
    Title: Design In-Memory File System
    Difficulty: Hard
"""

from typing import List


class FileSystem:

    def __init__(self):
        self.root = {}

    def ls(self, path: str) -> List[str]:
        path = self._split(path)
        node = self.root
        for component in path:
            node = node[component]
        if 0 in node:
            return [component]
        else:
            return list(sorted(node.keys()))

    def mkdir(self, path: str) -> None:
        path = self._split(path)
        node = self.root
        for component in path:
            if component not in node:
                node[component] = {}
            node = node[component]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = self._split(filePath)
        node = self.root
        for component in path:
            if component not in node:
                node[component] = {}
            node = node[component]
        if 0 in node:
            node[0] += content
        else:
            node[0] = content

    def readContentFromFile(self, filePath: str) -> str:
        path = self._split(filePath)
        node = self.root
        for component in path:
            if component not in node:
                node[component] = {}
            node = node[component]
        return node[0]

    def _split(self, path):
        if path == "/":
            return []
        return path[1:].split("/")


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
