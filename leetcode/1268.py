"""
    File: 1268.py
    Title: Search Suggestions System
    Difficulty: Medium
    URL: https://leetcode.com/problems/search-suggestions-system/
"""

import unittest

from typing import List

CHILDREN = 0


class Solution:
    def suggestedProducts(self,
                          products: List[str],
                          search_word: str) -> List[List[str]]:
        trie = {CHILDREN: []}
        for product in products:
            current = trie
            for c in product:
                if c not in current:
                    current[c] = {CHILDREN: []}

                next_children = current[c][CHILDREN]
                next_children.append(product)

                current[c][CHILDREN] = list(sorted(next_children))
                current = current[c]

        current = trie
        suggestions = [[] for _ in range(len(search_word))]
        for i, c in enumerate(search_word):
            if c not in current:
                break
            current = current[c]
            suggestions[i] = current[CHILDREN][:3]
        return suggestions


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        search_word = "mouse"
        # Output
        output = [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
        ]

        solution = Solution()
        self.assertEqual(solution.suggestedProducts(products, search_word),
                         output)

    def test_example2(self):
        # Input
        products = ["havana"]
        search_word = "havana"
        # Output
        output = [
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
        ]

        solution = Solution()
        self.assertEqual(solution.suggestedProducts(products, search_word),
                         output)

    def test_example3(self):
        # Input
        products = ["bags", "baggage", "banner", "box", "cloths"]
        search_word = "bags"
        # Output
        output = [
            ["baggage", "bags", "banner"],
            ["baggage", "bags", "banner"],
            ["baggage", "bags"],
            ["bags"],
        ]

        solution = Solution()
        self.assertEqual(solution.suggestedProducts(products, search_word),
                         output)

    def test_example4(self):
        # Input
        products = ["havana"]
        search_word = "tatiana"
        # Output
        output = [[], [], [], [], [], [], []]

        solution = Solution()
        self.assertEqual(solution.suggestedProducts(products, search_word),
                         output)


if __name__ == "__main__":
    unittest.main()
