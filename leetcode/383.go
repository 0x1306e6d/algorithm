// File: 383.go
// Title: Ransom Note
// Difficulty: Easy

package leetcode

func canConstruct(ransomNote string, magazine string) bool {
	m := make(map[rune]int)
	for _, r := range magazine {
		m[r] += 1
	}
	for _, r := range ransomNote {
		m[r] -= 1
		if m[r] < 0 {
			return false
		}
	}
	return true
}
