"""
    File: 640.py
    Title: Solve the Equation
    Difficulty: Medium
    URL: https://leetcode.com/problems/solve-the-equation/
"""

import unittest


class Solution:
    def solveEquation(self, equation: str) -> str:
        x = 0
        value = 0

        left = True
        sign = 1
        coefficient = None
        for i, c in enumerate(equation):
            if c == 'x':
                if coefficient is None:
                    x += sign if left else (-1 * sign)
                else:
                    if left:
                        x += (sign * coefficient)
                    else:
                        x += (-1 * sign * coefficient)
                coefficient = None
            elif (c == '+') or c == ('-'):
                if coefficient is not None:
                    if left:
                        value += (-1 * sign * coefficient)
                    else:
                        value += (sign * coefficient)
                    coefficient = None
                sign = 1 if c == '+' else -1
            elif c == '=':
                if coefficient is not None:
                    value += (-1 * sign * coefficient)
                left = False
                sign = 1
                coefficient = None
            else:
                if coefficient is None:
                    coefficient = int(c)
                else:
                    coefficient = (10 * coefficient) + int(c)

                if i == (len(equation) - 1):
                    value += (sign * coefficient)

        if x == 0 and value == 0:
            return "Infinite solutions"
        elif x == 0 and value != 0:
            return "No solution"
        elif x != 0 and value == 0:
            return "x=0"
        else:
            return "x={}".format(value // x)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        equation = "x+5-3+x=6+x-2"
        # Output
        output = "x=2"

        solution = Solution()
        self.assertEqual(solution.solveEquation(equation), output)

    def test_example2(self):
        # Input
        equation = "x=x"
        # Output
        output = "Infinite solutions"

        solution = Solution()
        self.assertEqual(solution.solveEquation(equation), output)

    def test_example3(self):
        # Input
        equation = "2x=x"
        # Output
        output = "x=0"

        solution = Solution()
        self.assertEqual(solution.solveEquation(equation), output)

    def test_example4(self):
        # Input
        equation = "2x+3x-6x=x+2"
        # Output
        output = "x=-1"

        solution = Solution()
        self.assertEqual(solution.solveEquation(equation), output)

    def test_example5(self):
        # Input
        equation = "x=x+2"
        # Output
        output = "No solution"

        solution = Solution()
        self.assertEqual(solution.solveEquation(equation), output)


if __name__ == "__main__":
    unittest.main()
