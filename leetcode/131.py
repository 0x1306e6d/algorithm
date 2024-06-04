"""
    File: 131.py
    Title: Palindrome Partitioning
    Difficulty: Medium
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []

        def palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrace(i, arr):
            if i == len(s):
                self.ans.append(arr.copy())
            else:
                for j in range(i, len(s)):
                    if palindrome(i, j):
                        arr.append(s[i : j + 1])
                        backtrace(j + 1, arr)
                        arr.pop()

        backtrace(0, [])

        return self.ans
