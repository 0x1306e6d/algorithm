"""
    File: 1533.py
    Title: Find the Index of the Large Integer
    Difficulty: Medium
"""


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader(object):
    # Compares the sum of arr[l..r] with the sum of arr[x..y]
    # return 1 if sum(arr[l..r]) > sum(arr[x..y])
    # return 0 if sum(arr[l..r]) == sum(arr[x..y])
    # return -1 if sum(arr[l..r]) < sum(arr[x..y])
    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        pass

    # Returns the length of the array
    def length(self) -> int:
        pass


class Solution:
    def getIndex(self, reader: "ArrayReader") -> int:
        left, right = 0, reader.length() - 1
        while left < right:
            third = (right - left) // 3
            lo = left + third
            hi = right - third
            result = reader.compareSub(left, lo, hi, right)
            if result == 0:
                left = lo + 1
                right = hi - 1
            elif result == 1:
                right = lo
            else:
                left = hi
        return left
