"""
    File: 394.py
    Title: Decode String
    Difficulty: Medium
"""


class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        def decode(i):
            num = ""
            while s[i] != "[":
                num += s[i]
                i += 1
            num = int(num)

            i += 1  # [

            ans = ""
            while s[i] != "]":
                c = s[i]
                if "a" <= c <= "z":
                    ans += c
                else:
                    decoded, i = decode(i)
                    ans += decoded
                i += 1
            return num * ans, i

        i = 0
        ans = ""
        while i < n:
            c = s[i]
            if "a" <= c <= "z":
                ans += c
            else:
                decoded, i = decode(i)
                ans += decoded
            i += 1
        return ans
