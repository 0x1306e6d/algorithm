"""
    File: 374.py
    Title: Guess Number Higher or Lower
    Difficulty: Easy
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            ans = guess(mid)
            if ans == 0:
                return mid
            if ans == -1:
                hi = mid - 1
            else:
                lo = mid + 1
