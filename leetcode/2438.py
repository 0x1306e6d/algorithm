"""
    File: 2438.py
    Title: Range Product Queries of Powers
    Difficulty: Medium
"""

from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7

        powers = []
        while n > 0:
            powers.append(n % 2)
            n = n // 2
        new_powers = []
        for i, bit in enumerate(powers):
            if bit == 1:
                new_powers.append(2**i)
        powers = new_powers
        preproduct = [1] * len(powers)
        preproduct[0] = powers[0]
        for i in range(1, len(powers)):
            preproduct[i] = preproduct[i - 1] * powers[i]

        ans = []
        for left, right in queries:
            if left == right:
                ans.append(powers[left] % mod)
            elif left == 0:
                ans.append(preproduct[right] % mod)
            else:
                leftproduct, rightproduct = preproduct[left - 1], preproduct[right]
                ans.append((rightproduct // leftproduct) % mod)
        return ans
