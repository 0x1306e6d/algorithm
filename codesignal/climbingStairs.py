def solution(n):
    if n == 1:
        return 1
    ways = [0] * n
    ways[1] = 1
    for i in range(2, n):
        ways[i] = ways[i - 1] + ways[i - 2] + 1
    return ways[-1] + 1
