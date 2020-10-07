"""
    File: 1220.py
    Title: Count Vowels Permutation
    Difficulty: Hard
    URL: https://leetcode.com/problems/count-vowels-permutation/
"""

import unittest


from collections import defaultdict


class Solution:

    MOD = 10**9 + 7

    def __init__(self):
        self.cache = defaultdict(dict)

    def countVowelPermutation(self, n: int) -> int:
        return self.count(n)

    def count(self, n: int, vowel: str = None) -> int:
        if n == 0:
            return 1

        if vowel in self.cache[n]:
            return self.cache[n][vowel]

        count = 0
        if vowel == 'a':
            count = self.count(n - 1, 'e')
        elif vowel == 'e':
            count = self.count(n - 1, 'a')
            count += self.count(n - 1, 'i')
        elif vowel == 'i':
            count = self.count(n - 1, 'a')
            count += self.count(n - 1, 'e')
            count += self.count(n - 1, 'o')
            count += self.count(n - 1, 'u')
        elif vowel == 'o':
            count = self.count(n - 1, 'i')
            count += self.count(n - 1, 'u')
        elif vowel == 'u':
            count = self.count(n - 1, 'a')
        elif vowel is None:
            count = self.count(n - 1, 'a')
            count += self.count(n - 1, 'e')
            count += self.count(n - 1, 'i')
            count += self.count(n - 1, 'o')
            count += self.count(n - 1, 'u')
        count %= self.MOD
        self.cache[n][vowel] = count
        return count


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 1
        # Output
        output = 5

        solution = Solution()
        self.assertEqual(solution.countVowelPermutation(n), output)

    def test_example2(self):
        # Input
        n = 2
        # Output
        output = 10

        solution = Solution()
        self.assertEqual(solution.countVowelPermutation(n), output)

    def test_example3(self):
        # Input
        n = 5
        # Output
        output = 68

        solution = Solution()
        self.assertEqual(solution.countVowelPermutation(n), output)


if __name__ == "__main__":
    unittest.main()
