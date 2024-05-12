"""
    File: 38.py
    Title: Count and Say
    Difficulty: Medium
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        ans = ""
        count = 1
        say = prev[0]
        for i in range(1, len(prev)):
            c = prev[i]
            if c == say:
                count += 1
            else:
                ans += f"{count}{say}"
                count = 1
                say = c
        ans += f"{count}{say}"
        return ans
