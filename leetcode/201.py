"""
    File: 201.py
    Title: Bitwise AND of Numbers Range
    Difficulty: Medium
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bit = 1 << 30
        ans = 0
        while bit:
            if left & bit == bit and right & bit == bit:
                ans += bit
            elif left & bit == 0 and right & bit == 0:
                pass
            else:
                break
            bit = bit >> 1
        return ans
