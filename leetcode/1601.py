"""
    File: 1601.py
    Title: Maximum Number of Achievable Transfer Requests
    Difficulty: Hard
"""

from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.ans = 0

        def backtrace(indegree, idx, count):
            if idx == len(requests):
                for d in indegree:
                    if d != 0:
                        return
                self.ans = max(self.ans, count)
                return

            u, v = requests[idx]
            indegree[u] += 1
            indegree[v] -= 1
            backtrace(indegree, idx + 1, count + 1)
            indegree[u] -= 1
            indegree[v] += 1

            backtrace(indegree, idx + 1, count)

        indegree = [0] * n
        backtrace(indegree, 0, 0)

        return self.ans
