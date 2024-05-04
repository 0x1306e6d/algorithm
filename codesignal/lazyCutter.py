def solution(n):
    memo = [0] * (n + 1)
    memo[1] = 2
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + i
    return memo[n]
