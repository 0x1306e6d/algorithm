"""
    File: 935.py
    Title: Knight Dialer
    Difficulty: Medium
"""


class Solution:
    def knightDialer(self, n: int) -> int:
        move = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }
        mod = 10**9 + 7
        memo = [1] * 10
        for _ in range(n - 1):
            copy = memo.copy()
            for i in range(10):
                for j in move[i]:
                    memo[i] += copy[j]
                    memo[i] %= mod
            for i in range(10):
                memo[i] -= copy[i]
        return sum(memo) % mod
