"""
    File: 729.py
    Title: My Calendar I
    Difficulty: Medium
    URL: https://leetcode.com/problems/my-calendar-i/
"""

import unittest


class MyCalendar:
    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> bool:
        for book in self.books:
            s, e = book
            if (s <= start < e) or (s < end < e) or (start <= s < end):
                return False
        self.books.append((start, end))
        return True


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertFalse(cal.book(15, 25))
        self.assertTrue(cal.book(20, 30))


if __name__ == "__main__":
    unittest.main()
