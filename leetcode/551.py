"""
    File: 551.py
    Title: Student Attendance Record I
    Difficulty: Easy
    URL: https://leetcode.com/problems/student-attendance-record-i/
"""

import unittest


class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for c in s:
            if c == 'A':
                absent += 1
                if absent >= 2:
                    return False
            if c == 'L':
                late += 1
                if late >= 3:
                    return False
            else:
                late = 0
        return True


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "PPALLP"
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.checkRecord(s), output)

    def test_example2(self):
        # Input
        s = "PPALLL"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.checkRecord(s), output)


if __name__ == "__main__":
    unittest.main()
