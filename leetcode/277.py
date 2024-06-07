"""
    File: 277.py
    Title: Find the Celebrity
    Difficulty: Medium
"""


# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb = 0
        for i in range(1, n):
            if knows(celeb, i):
                celeb = i
        for i in range(n):
            if i == celeb:
                continue
            if knows(celeb, i) or not knows(i, celeb):
                return -1
        return celeb
