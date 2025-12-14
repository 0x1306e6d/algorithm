// File: 2469.go
// Title: Convert the Temperature
// Difficulty: Easy

package leetcode

func convertTemperature(celsius float64) []float64 {
	kelvin := celsius + 273.15
	fahrenheit := celsius*1.80 + 32
	return []float64{kelvin, fahrenheit}
}
