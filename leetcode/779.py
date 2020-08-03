"""
    File: 779.py
    Title: K-th Symbol in Grammar
    Difficulty: Medium
    URL: https://leetcode.com/problems/k-th-symbol-in-grammar/
"""

import unittest


class Solution:

    sheet = {1: '0', 2: '01', 3: '0110'}

    def kthGrammar(self, N: int, K: int) -> int:
        return self.find(N, K)

    def find(self, n: int, index: int) -> int:
        if n < 4:
            return int(self.sheet[n][index - 1])

        length = 2 ** (n - 1)
        half = length // 2
        quater = length // 4

        if index <= half:
            return self.find(n - 1, index)
        elif half < index <= half + quater:
            return self.find(n - 1, index - half + quater)
        else:
            return self.find(n - 2, index - half - quater)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        N = 1
        K = 1
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.kthGrammar(N, K), output)

    def test_example2(self):
        # Input
        N = 2
        K = 1
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.kthGrammar(N, K), output)

    def test_example3(self):
        # Input
        N = 2
        K = 2
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.kthGrammar(N, K), output)

    def test_example4(self):
        # Input
        N = 4
        K = 5
        # Output
        output = 1

        solution = Solution()
        self.assertEqual(solution.kthGrammar(N, K), output)


if __name__ == "__main__":
    unittest.main()
