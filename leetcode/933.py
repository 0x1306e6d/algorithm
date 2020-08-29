"""
    File: 933.py
    Title: Number of Recent Calls
    Difficulty: Easy
    URL: https://leetcode.com/problems/number-of-recent-calls/
"""

import bisect
import unittest


class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)

        recent_requests = 0
        i = bisect.bisect(self.requests, t) - 1
        while i >= 0:
            r = self.requests[i]
            if (t - 3000) <= r:
                recent_requests += 1
            else:
                break
            i -= 1
        return recent_requests


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        obj = RecentCounter()

        self.assertEqual(obj.ping(1), 1)
        self.assertEqual(obj.ping(100), 2)
        self.assertEqual(obj.ping(3001), 3)
        self.assertEqual(obj.ping(3002), 3)


if __name__ == "__main__":
    unittest.main()
