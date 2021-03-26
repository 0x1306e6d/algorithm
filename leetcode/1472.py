"""
    File: 1472.py
    Title: Design Browser History
    Difficulty: Medium
    URL: https://leetcode.com/problems/design-browser-history/
"""

import unittest


class Node:
    def __init__(self, url: str, back: "Node", forward: "Node") -> None:
        self.url = url
        self.back = back
        self.forward = forward


class BrowserHistory:
    def __init__(self, homepage: str):
        self.root = Node(homepage, None, None)
        self.current = self.root

    def visit(self, url: str) -> None:
        node = Node(url, self.current, None)
        self.current.forward = node
        self.current = node

    def back(self, steps: int) -> str:
        for step in range(steps):
            if self.current.back is None:
                break
            self.current = self.current.back
        return self.current.url

    def forward(self, steps: int) -> str:
        for step in range(steps):
            if self.current.forward is None:
                break
            self.current = self.current.forward
        return self.current.url


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        browser_history = BrowserHistory("leetcode.com")
        browser_history.visit("google.com")
        browser_history.visit("facebook.com")
        browser_history.visit("youtube.com")
        self.assertEqual(browser_history.back(1), "facebook.com")
        self.assertEqual(browser_history.back(1), "google.com")
        self.assertEqual(browser_history.forward(1), "facebook.com")
        browser_history.visit("linkedin.com")
        self.assertEqual(browser_history.forward(2), "linkedin.com")
        self.assertEqual(browser_history.back(2), "google.com")
        self.assertEqual(browser_history.back(7), "leetcode.com")


if __name__ == "__main__":
    unittest.main()
