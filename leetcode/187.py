"""
    File: 187.py
    Title: Repeated DNA Sequences
    Difficulty: Medium
    URL: https://leetcode.com/problems/repeated-dna-sequences/
"""

import unittest

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = {}
        for i in range(0, len(s) - 10 + 1):
            substring = s[i:i + 10]
            if substring not in counter:
                counter[substring] = 1
            else:
                counter[substring] += 1
        return list(map(lambda kv: kv[0],
                        filter(lambda kv: kv[1] > 1, counter.items())))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        # Output
        output = ["AAAAACCCCC", "CCCCCAAAAA"]

        solution = Solution()
        self.assertEqual(solution.findRepeatedDnaSequences(s), output)


if __name__ == "__main__":
    unittest.main()
