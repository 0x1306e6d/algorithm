"""
    File: 6.py
    Title: Zigzag Conversion
    Difficulty: Medium
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        i = 0
        while i < len(s):
            for j in range(numRows):
                if i < len(s):
                    ans[j].append(s[i])
                    i += 1
                else:
                    break
            for j in range(1, numRows - 1):
                if i < len(s):
                    ans[numRows - j - 1].append(s[i])
                    i += 1
                else:
                    break
        return "".join(map(lambda x: "".join(x), ans))
