package day2

func IsNotAllowedDiff(diff int) bool {
	return diff > 3 || diff < -3 || diff == 0
}

func IsAllowedDiff(diff int) bool {
	return !IsNotAllowedDiff(diff)
}