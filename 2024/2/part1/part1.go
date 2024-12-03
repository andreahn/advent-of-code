package main

import (
	day2 "github.com/andreahn/advent-of-code-2024/2/shared"
	"github.com/andreahn/advent-of-code-2024/helpers"
)


func Part1(inputPath string) int {
	data := helpers.GetIntegerMatrix(inputPath)

	safeCount := 0

	for _,row  := range data {
		isSafe := checkIfSafe(row)
		if isSafe {
			safeCount++
		}
	}
	return safeCount
}

func checkIfSafe(data []int) bool {
	var previousNumber int
	var isIncreasing bool
	setIncreasing := true

	for i, number := range data {

		if i == 0 {
			previousNumber = number
			continue
		} 
		
		if setIncreasing {
			isIncreasing = number > previousNumber
			setIncreasing = false
		}
		
		diff := number - previousNumber

		if day2.IsNotAllowedDiff(diff) || isIncreasing != (number > previousNumber) {
			return false
		}
		previousNumber = number
	}
	return true
}