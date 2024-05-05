from collections import defaultdict


def solution(s, t):
    chars = defaultdict(int)
    for c in s:
        chars[c] += 1
    ans = ""
    for c in t:
        for i in range(chars[c]):
            ans += c
    return ans
