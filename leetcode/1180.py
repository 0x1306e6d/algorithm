"""
    File: 1180.py
    Title: Count Substrings with Only One Distinct Letter
    Difficulty: Easy
"""


class Solution:
    def countLetters(self, s: str) -> int:
        left, right, ans = 0, 1, 0
        while right < len(s):
            c = s[right]
            if c != s[left]:
                n = right - left
                ans += (n * (n + 1)) // 2
                left = right
            right += 1
        n = right - left
        ans += (n * (n + 1)) // 2
        return ans
