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
	pages := strings.TrimRight(splitData[1], "\n")
	result := 0

	for _,page  := range strings.Split(pages, "\n") {
		hasBeenSwapped := false
		numbers := strings.Split(page, ",")

		for i := 0; i < len(numbers); i++ {
			num := numbers[i]

			if (i == len(numbers) - 1) {
				break
			}
			ruleForNum := rules[num]

			if len(ruleForNum) == 0 {
				continue
			}

			remainingNumbers := numbers[i + 1:]

			for _, n := range remainingNumbers {
				isPresent := slices.Contains(ruleForNum, n)
				if isPresent {
					// swap
					realIndex := i + slices.Index(remainingNumbers, n) + 1
					numbers[i] = n
					numbers[realIndex] = num
					i--
					hasBeenSwapped = true
					break
				}
			}
		}
		if (hasBeenSwapped) {
			result += helpers.StringToInt(numbers[len(numbers)/2])
		}
	}

	return result
}
