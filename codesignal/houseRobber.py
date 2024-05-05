def solution(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    memo = [[0, 0] for _ in range(len(nums))]
    memo[0][0] = nums[0]
    memo[1][0] = nums[1]
    memo[1][1] = nums[0]
    for i in range(2, len(nums)):
        memo[i][0] = max(memo[i - 2][0], memo[i - 1][1]) + nums[i]
        memo[i][1] = max(memo[i - 1])
    return max(memo[len(nums) - 1])
