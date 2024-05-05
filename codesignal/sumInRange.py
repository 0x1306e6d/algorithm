def solution(nums, queries):
    psum = [0] * len(nums)
    psum[0] = nums[0]
    for i in range(1, len(nums)):
        psum[i] = psum[i - 1] + nums[i]

    ans = 0
    mod = pow(10, 9) + 7
    for s, e in queries:
        if s == 0:
            ans += psum[e]
        else:
            ans += psum[e] - psum[s - 1]
    return ans % mod
