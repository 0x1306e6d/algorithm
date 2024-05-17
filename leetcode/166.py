"""
    File: 166.py
    Title: Fraction to Recurring Decimal
    Difficulty: Medium
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        sign = (numerator < 0) != (denominator < 0)

        numerator = abs(numerator)
        denominator = abs(denominator)
        quotient = numerator // denominator
        remainder = numerator % denominator

        if remainder == 0:
            return f"-{quotient}" if sign else str(quotient)

        integer = quotient
        index = 0
        remainders = {}
        fractions = []
        cycle = True
        while remainder not in remainders:
            remainders[remainder] = index
            index += 1

            quotient = (remainder * 10) // denominator
            remainder = (remainder * 10) % denominator
            fractions.append(quotient)
            if remainder == 0:
                cycle = False
                break
        if cycle:
            fractions.insert(remainders[remainder], "(")
            fractions.append(")")
        return f'{"-" if sign else ""}{integer}.{"".join(map(str, fractions))}'
