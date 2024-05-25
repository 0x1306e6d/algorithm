"""
    File: 76.py
    Title: Minimum Window Substring
    Difficulty: Hard
"""


def new_dict():
    d = {}
    for c in range(ord("a"), ord("z") + 1):
        d[chr(c)] = 0
    for c in range(ord("A"), ord("Z") + 1):
        d[chr(c)] = 0
    return d


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:
            return ""

        target = {}
        for c in t:
            if c not in target:
                target[c] = 0
            target[c] += 1

        def include(window):
            for c in target:
                if window[c] < target[c]:
                    return False
            return True

        ans = None
        window = new_dict()
        left, right = 0, -1
        while right < m - 1:
            for right in range(right + 1, m):
                c = s[right]
                window[c] += 1
                if include(window):
                    break
            for left in range(left, m):
                c = s[left]
                window[c] -= 1
                if not include(window):
                    window[c] += 1
                    break
            if not include(window):
                return ""
            if ans is None or right - left + 1 < len(ans):
                ans = s[left : right + 1]
        if ans is None:
            return ""
        return ans
