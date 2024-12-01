package main

import (
	"github.com/andreahn/advent-of-code-2024/1/shared"
)

func Part2(inputPath string) int {
	first, second := day1.GetInputArrays(inputPath)

	occurences := make(map[int]int)

	for _, value := range second {
		occurences[value] += 1
	}

	similarityScore := 0

	for _, value := range first {
		similarityScore += occurences[value] * value
	}
	return similarityScore
}