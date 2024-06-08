"""
    File: 340.py
    Title: Longest Substring with At Most K Distinct Characters
    Difficulty: Medium
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        left = right = ans = 0
        chars = {}
        while right < n:
            c = s[right]
            if c not in chars:
                chars[c] = 0
            chars[c] += 1
            while len(chars) > k:
                c = s[left]
                chars[c] -= 1
                if chars[c] == 0:
                    del chars[c]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
