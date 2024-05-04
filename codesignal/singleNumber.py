def solution(nums):
    res = 0
    for num in nums:
        res = res ^ num
    return res
