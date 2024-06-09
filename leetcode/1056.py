"""
    File: 1056.py
    Title: Confusing Number
    Difficulty: Easy
"""


class Solution:
    def confusingNumber(self, n: int) -> bool:
        nums = {
            "0": "0",
            "1": "1",
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": "9",
            "7": None,
            "8": "8",
            "9": "6",
        }
        num = str(n)
        rotated = ""
        for i, digit in enumerate(num):
            rotated_digit = nums[digit]
            if rotated_digit is None:
                return False
            rotated = rotated_digit + rotated
        return rotated != num
