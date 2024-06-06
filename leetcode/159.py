"""
    File: 159.py
    Title: Longest Substring with At Most Two Distinct Characters
    Difficulty: Medium
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        ans = left = right = 0
        chars = {}
        while right < n:
            c = s[right]
            if c not in chars:
                chars[c] = 0
            chars[c] += 1
            while len(chars) > 2:
                c2 = s[left]
                chars[c2] -= 1
                if chars[c2] == 0:
                    del chars[c2]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
