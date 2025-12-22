package leetcode

func minSubArrayLen(target int, nums []int) int {
	ans := 987654321
	window := 0
	windowStart := 0
	for i, num := range nums {
		window += num
		for window >= target {
			ans = min(ans, i-windowStart+1)
			window -= nums[windowStart]
			windowStart += 1
		}
	}
	if ans == 987654321 {
		return 0
	}
	return ans
}
