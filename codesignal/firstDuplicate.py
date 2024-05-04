def solution(a):
    memo = {}
    for n in a:
        if n in memo:
            return n
        memo[n] = True
    return -1
