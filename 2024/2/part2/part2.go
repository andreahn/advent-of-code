package main

import (
	day2 "github.com/andreahn/advent-of-code-2024/2/shared"
	"github.com/andreahn/advent-of-code-2024/helpers"
)

func Part2(inputPath string) int {
	data := helpers.GetIntegerMatrix(inputPath)

	safeCount := 0

	for _, row := range data {
		isSafe := checkIfSafeWithSkip(row)
		if isSafe {
			safeCount++
		}
	}
	return safeCount
}

func checkIfSafeWithSkip(data []int) bool {

	i, success := checkIfSafe(data, -1)
	if success {
		return true
	} else {
		_, skipIndex := checkIfSafe(data, i)

		if skipIndex {
			return true
		}

		_, skipBeforeIndex := checkIfSafe(data, i-1)

		if skipBeforeIndex {
			return true
		}

		if i == 2 {
			_, skipFirst := checkIfSafe(data, i-2)

			return skipFirst
		}

		if i < (len(data) - 1) {
			_, skipNext := checkIfSafe(data, i+1)

			return skipNext
		}

		return false
	}
}

func checkIfSafe(data []int, skipIndex int) (int, bool) {
	var previousNumber int
	var isIncreasing bool
	increasingNotSet := true
	isFirst := true

	for i, number := range data {
		if i == skipIndex {
			continue
		}

		if isFirst {
			previousNumber = number
			isFirst = false
			continue
		}

		if increasingNotSet {
			isIncreasing = number > previousNumber
			increasingNotSet = false
		}

		diff := number - previousNumber
		localIncrease := number > previousNumber

		if day2.IsNotAllowedDiff(diff) || (isIncreasing != localIncrease) {
			return i, false
		}
		previousNumber = number
	}
	return -1, true
}
