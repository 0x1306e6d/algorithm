"""
    File: 1291.py
    Title: Sequential Digits
    Difficulty: Medium
"""

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def get_start(n):
            ans = 1
            for i in range(2, n + 1):
                ans = (ans * 10) + i
            return ans

        def get_increment(n):
            ans = 1
            for _ in range(2, n + 1):
                ans = (ans * 10) + 1
            return ans

        ans = []
        i = 2
        while i < 10:
            num = get_start(i)
            if num > high:
                break
            increment = get_increment(i)
            while (num % 10) > 0:
                if num > high:
                    break
                if low <= num <= high:
                    ans.append(num)
                num += increment
            i += 1
        return ans
