from collections import defaultdict


def solution(s):
    if len(s) < 10:
        return []
    memo = defaultdict(int)
    for i in range(len(s) - 10 + 1):
        memo[s[i : i + 10]] += 1
    ans = []
    for seq in sorted(memo):
        if memo[seq] > 1:
            ans.append(seq)
    return ans
