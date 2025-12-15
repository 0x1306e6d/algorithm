// File: 88.go
// Title: Merge Sorted Array
// Difficulty: Easy

package leetcode

func merge(nums1 []int, m int, nums2 []int, n int) {
	i := m - 1
	j := n - 1
	k := m + n - 1
	for {
		if i < 0 && j < 0 {
			break
		} else if i < 0 {
			nums1[k] = nums2[j]
			j -= 1
		} else if j < 0 {
			nums1[k] = nums1[i]
			i -= 1
		} else if nums1[i] > nums2[j] {
			nums1[k] = nums1[i]
			i -= 1
		} else {
			nums1[k] = nums2[j]
			j -= 1
		}
		k -= 1
	}
}
