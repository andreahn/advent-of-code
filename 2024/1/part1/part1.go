package main

import (
	"slices"
	"github.com/andreahn/advent-of-code-2024/1/shared"
)

func Part1(inputPath string) int {
	first, second := day1.GetInputArrays(inputPath)

	slices.Sort(first)
	slices.Sort(second)

	totalDistance := 0

	for i, firstVal := range first {
		secondVal := second[i]

		if secondVal < firstVal {
			totalDistance += firstVal - secondVal
			} else {
			totalDistance += secondVal - firstVal
		}
	}
	return totalDistance
}