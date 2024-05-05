def solution(nums, k):
    memo = {}
    for i, n in enumerate(nums):
        if n in memo:
            if i - memo[n] <= k:
                return True
        memo[n] = i
    return False
