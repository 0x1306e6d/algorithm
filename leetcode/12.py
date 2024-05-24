"""
    File: 12.py
    Title: Integer to Roman
    Difficulty: Medium
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = "M" * (num // 1000)

        num %= 1000
        h = num // 100
        hundreds = ""
        if h == 4:
            hundreds = "CD"
        elif h == 9:
            hundreds = "CM"
        else:
            if h >= 5:
                hundreds = "D"
                h -= 5
            hundreds += "C" * h

        num %= 100
        t = num // 10
        tens = ""
        if t == 4:
            tens = "XL"
        elif t == 9:
            tens = "XC"
        else:
            if t >= 5:
                tens = "L"
                t -= 5
            tens += "X" * t

        num %= 10
        o = num
        ones = ""
        if o == 4:
            ones = "IV"
        elif o == 9:
            ones = "IX"
        else:
            if o >= 5:
                ones = "V"
                o -= 5
            ones += "I" * o

        return thousands + hundreds + tens + ones
