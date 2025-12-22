package leetcode

import (
	"fmt"
	"strconv"
)

func summaryRanges(nums []int) []string {
	if len(nums) == 0 {
		return []string{}
	}

	ans := []string{}
	start := 0
	end := len(nums) - 1
	for i := 1; i <= end; i++ {
		if nums[i] == nums[i-1]+1 {
			continue
		} else {
			if i-start == 1 {
				ans = append(ans, strconv.Itoa(nums[start]))
			} else {
				ans = append(ans, fmt.Sprintf("%d->%d", nums[start], nums[i-1]))
			}
			start = i
		}
	}
	if start == end {
		ans = append(ans, strconv.Itoa(nums[start]))
	} else {
		ans = append(ans, fmt.Sprintf("%d->%d", nums[start], nums[end]))
	}
	return ans
}
