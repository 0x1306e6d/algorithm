"""
    File: 295.py
    Title: Find Median from Data Stream
    Difficulty: Hard
"""


def bisect_left(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        i = bisect_left(self.arr, num)
        self.arr.insert(i, num)

    def findMedian(self) -> float:
        if len(self.arr) == 1:
            return self.arr[0]

        mid = len(self.arr) // 2
        if len(self.arr) % 2 == 0:
            return (self.arr[mid] + self.arr[mid - 1]) / 2
        else:
            return self.arr[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
