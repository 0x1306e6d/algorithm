"""
    File: 165.py
    Title: Compare Version Numbers
    Difficulty: Medium
    URL: https://leetcode.com/problems/compare-version-numbers/description/
"""

import unittest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = 0
        j = 0
        while i < len(version1) or j < len(version2):
            v1 = ''
            for ii in range(i, len(version1)):
                i += 1
                v = version1[ii]
                if v == '.':
                    break
                v1 += v
            if v1 == '':
                v1 = 0
            else:
                v1 = int(v1)

            v2 = ''
            for jj in range(j, len(version2)):
                j += 1
                v = version2[jj]
                if v == '.':
                    break
                v2 += v
            if v2 == '':
                v2 = 0
            else:
                v2 = int(v2)
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        version1 = "1.01"
        version2 = "1.001"
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.compareVersion(version1, version2), output)

    def test_example2(self):
        # Input
        version1 = "1.0"
        version2 = "1.0.0"
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.compareVersion(version1, version2), output)

    def test_example3(self):
        # Input
        version1 = "0.1"
        version2 = "1.1"
        # Output
        output = -1

        solution = Solution()
        self.assertEqual(solution.compareVersion(version1, version2), output)


if __name__ == "__main__":
    unittest.main()
