"""
    File: 1309.py
    Title: Decrypt String from Alphabet to Integer Mapping
    Difficulty: Easy
    URL: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
"""

import unittest


class Solution:
    def freqAlphabets(self, s: str) -> str:
        length = len(s)

        ord_a = ord('a')

        def chrs(c: str) -> str:
            return chr(ord_a + int(c) - 1)

        def decrypt(i: int) -> str:
            if (i + 2) >= length:
                return i + 1, chrs(s[i])
            if s[i + 2] == '#':
                return i + 3, chrs(s[i] + s[i + 1])
            return i + 1, chrs(s[i])

        i = 0
        ret = ''
        while i < length:
            i, formed = decrypt(i)
            ret += formed
        return ret


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "10#11#12"
        # Output
        output = "jkab"

        solution = Solution()
        self.assertEqual(solution.freqAlphabets(s), output)

    def test_example2(self):
        # Input
        s = "1326#"
        # Output
        output = "acz"

        solution = Solution()
        self.assertEqual(solution.freqAlphabets(s), output)

    def test_example3(self):
        # Input
        s = "25#"
        # Output
        output = "y"

        solution = Solution()
        self.assertEqual(solution.freqAlphabets(s), output)

    def test_example4(self):
        # Input
        s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
        # Output
        output = "abcdefghijklmnopqrstuvwxyz"

        solution = Solution()
        self.assertEqual(solution.freqAlphabets(s), output)


if __name__ == "__main__":
    unittest.main()
