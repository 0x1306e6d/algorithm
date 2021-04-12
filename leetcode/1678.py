"""
    File: 1678.py
    Title: Goal Parser Interpretation
    Difficulty: Easy
    URL: https://leetcode.com/problems/goal-parser-interpretation/
"""

import unittest


class Solution:
    def interpret(self, command: str) -> str:
        interpreted = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                interpreted += 'G'
                i += 1
            else:
                if command[i + 1] == ')':
                    interpreted += 'o'
                    i += 2
                else:
                    interpreted += 'al'
                    i += 4
        return interpreted


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        command = "G()(al)"
        # Output
        output = "Goal"

        solution = Solution()
        self.assertEqual(solution.interpret(command), output)

    def test_example2(self):
        # Input
        command = "G()()()()(al)"
        # Output
        output = "Gooooal"

        solution = Solution()
        self.assertEqual(solution.interpret(command), output)

    def test_example3(self):
        # Input
        command = "(al)G(al)()()G"
        # Output
        output = "alGalooG"

        solution = Solution()
        self.assertEqual(solution.interpret(command), output)


if __name__ == "__main__":
    unittest.main()
