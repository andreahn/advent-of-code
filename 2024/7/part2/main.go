package main

import (
	"fmt"
	"strings"

	"github.com/andreahn/advent-of-code-2024/helpers"
)

func main() {
	inputPath := "../input/input.txt"
	fmt.Println(SolvePuzzle(inputPath))
}

func SolvePuzzle(inputPath string) int {

	data := helpers.ReadInputAsString(inputPath)
	data = strings.TrimRight(data, "\n")
	result := 0
	for _, v := range strings.Split(data, "\n") {
		splitString := strings.Split(string(v), ":")
		leftValue := helpers.StringToInt(splitString[0])
		rightValues := make([]int, 0)
		
		for _, num := range strings.Split(strings.TrimLeft(splitString[1], " "), " ") {
			rightValues = append(rightValues, helpers.StringToInt(num))
		}
		result += tryAllCombinations(leftValue, rightValues)
	}
	return result
}


func tryAllCombinations(sol int, numbers []int) int {
	if tryAllCombinatiosnRec(sol, numbers[0], numbers[1:]) {
		return sol
	}

	return 0
}

func tryAllCombinatiosnRec(sol int, currentTotal int, numbers []int) bool {
	if len(numbers) == 0 {
		return currentTotal == sol
	}
	num := numbers[0]

	concatenatedNumber := helpers.StringToInt(fmt.Sprintf("%d%d", currentTotal, num))

	if len(numbers) == 1 {
		return sol == currentTotal + num || sol == currentTotal * num || concatenatedNumber == sol
	}

	remainingNumbers := numbers[1:]
	
	if tryAllCombinatiosnRec(sol, currentTotal + num, remainingNumbers) {
		return true
	}
	if tryAllCombinatiosnRec(sol, currentTotal * num, remainingNumbers) {
		return true
	}
	if tryAllCombinatiosnRec(sol, concatenatedNumber, remainingNumbers) {
		return true
	}
	return false
}
