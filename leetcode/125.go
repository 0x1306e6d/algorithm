// File: 125.go
// Title: Valid Palindrome
// Difficulty: Easy

package leetcode

import (
	"strings"
	"unicode"
)

func isPalindrome(s string) bool {
	alphanumeric := ""
	for _, r := range s {
		if unicode.IsLetter(r) || unicode.IsNumber(r) {
			alphanumeric += strings.ToLower(string(r))
		}
	}
	length := len(alphanumeric)
	for i := 0; i < length/2; i++ {
		if alphanumeric[i] != alphanumeric[length-i-1] {
			return false
		}
	}
	return true
}
