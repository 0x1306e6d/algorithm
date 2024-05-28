"""
    File: 273.py
    Title: Integer to English Words
    Difficulty: Hard
"""

from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        dictionary = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        suffixes = {
            "": "Thousand",
            "Thousand": "Million",
            "Million": "Billion",
            "Billion": "Trillion",
        }

        def to_string(n, suffix):
            ans = []
            if n >= 1000:
                ans = to_string(n // 1000, suffixes[suffix])
                n = n % 1000
            if n == 0:
                return ans
            if n >= 100:
                ans.append(dictionary[n // 100])
                ans.append("Hundred")
                n = n % 100
            if n == 0:
                pass
            elif n in dictionary:
                ans.append(dictionary[n])
            else:
                ans.append(dictionary[(n // 10) * 10])
                ans.append(dictionary[n % 10])
            if suffix:
                ans.append(suffix)
            return ans

        return " ".join(to_string(num, ""))
