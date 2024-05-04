def solution(a):
    memo = {}
    for n in a:
        if n in memo:
            return True
        memo[n] = True
    return False
