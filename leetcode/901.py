"""
    File: 901.py
    Title: Online Stock Span
    Difficulty: Medium
    URL: https://leetcode.com/problems/online-stock-span/
"""

import unittest


class StockSpanner:
    def __init__(self):
        self.history = []

    def next(self, price: int) -> int:
        count = 1
        i = len(self.history) - 1
        while i >= 0:
            if self.history[i][0] <= price:
                count += self.history[i][1]
                i -= self.history[i][1]
            else:
                break
        self.history.append((price, count))
        return count


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        spanner = StockSpanner()

        self.assertEqual(spanner.next(100), 1)
        self.assertEqual(spanner.next(80), 1)
        self.assertEqual(spanner.next(60), 1)
        self.assertEqual(spanner.next(70), 2)
        self.assertEqual(spanner.next(60), 1)
        self.assertEqual(spanner.next(75), 4)
        self.assertEqual(spanner.next(85), 6)


if __name__ == "__main__":
    unittest.main()
