"""
    File: 4.py
    Title: Median of Two Sorted Arrays
    Difficulty: Hard
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)

        def median(k, start1, end1, start2, end2):
            if start1 > end1:
                return nums2[k - start1]
            if start2 > end2:
                return nums1[k - start2]

            mid1, mid2 = (start1 + end1) // 2, (start2 + end2) // 2
            val1, val2 = nums1[mid1], nums2[mid2]

            if mid1 + mid2 < k:
                if val1 > val2:
                    return median(k, start1, end1, mid2 + 1, end2)
                else:
                    return median(k, mid1 + 1, end1, start2, end2)
            else:
                if val1 > val2:
                    return median(k, start1, mid1 - 1, start2, end2)
                else:
                    return median(k, start1, end1, start2, mid2 - 1)

        if (len1 + len2) % 2 == 0:
            a = median((len1 + len2) // 2 - 1, 0, len1 - 1, 0, len2 - 1)
            b = median((len1 + len2) // 2, 0, len1 - 1, 0, len2 - 1)
            return (a + b) / 2
        else:
            return median((len1 + len2) // 2, 0, len1 - 1, 0, len2 - 1)
