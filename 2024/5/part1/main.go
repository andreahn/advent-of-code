package main

import (
	"fmt"
	"slices"
	"strings"

	day5 "github.com/andreahn/advent-of-code-2024/5/shared"
	"github.com/andreahn/advent-of-code-2024/helpers"
)

func main() {
	inputPath := "../input/input.txt"
	fmt.Println(SolvePuzzle(inputPath))
}

func SolvePuzzle(inputPath string) int {
	data := helpers.ReadInputAsString(inputPath)

	splitData := strings.Split(data, "\n\n")

	rules := day5.GatherRules(splitData[0])

	toTest := strings.TrimRight(splitData[1], "\n")

	result := 0

	for _,order  := range strings.Split(toTest, "\n") {
		isCorrect := true

		numbers := strings.Split(order, ",")

		for i,num := range numbers {
			if (i == len(numbers) - 1) || !isCorrect {
				break
			}
			ruleForNum := rules[num]

			remainingNumbers := numbers[i + 1:]

			for _, n := range remainingNumbers {
				if slices.Contains(ruleForNum, n) {
					isCorrect = false
					break
				}
			}
		}

		if isCorrect {
			result += helpers.StringToInt(numbers[len(numbers)/2])
		}
	}

	return result
}
