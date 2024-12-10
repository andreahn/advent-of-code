package main

import (
	"fmt"

	"github.com/andreahn/advent-of-code-2024/helpers"
)

func main() {
	inputPath := "../input/input.txt"
	fmt.Println(SolvePuzzle(inputPath))
}

var maxX  int = 0
var maxY  int = 0


func SolvePuzzle(inputPath string) int {
	data := helpers.GetIntegerMatrixNoSpacing(inputPath)
	maxX = len(data) - 1
	maxY = len(data[0]) - 1

	sum := 0

	for x, line := range data {
		for y, val := range line {
			if val == 0 {
				sum += (findTrailsFromTrailHead(data, x, y))
			}
		}
	}
	return sum
}


func findTrailsFromTrailHead(forestMap [][]int, x int, y int) int{
	currentAltitude := forestMap[x][y]
	res := 0

	if currentAltitude == 9 {
		return 1
	}
	
	if isInRange(x + 1, y) && forestMap[x + 1][y] == currentAltitude + 1 {
		res += findTrailsFromTrailHead(forestMap, x + 1, y)
	}

	if isInRange(x - 1, y) && forestMap[x - 1][y] == currentAltitude + 1 {
		res += findTrailsFromTrailHead(forestMap, x - 1, y)
	}

	if isInRange(x, y + 1) && forestMap[x][y + 1] == currentAltitude + 1 {
		res += findTrailsFromTrailHead(forestMap, x, y + 1)
	}

	if isInRange(x, y - 1) && forestMap[x][y - 1] == currentAltitude + 1 {
		res += findTrailsFromTrailHead(forestMap, x, y - 1)
	}

	return res
}

func isInRange(x int, y int) bool {
	return x >= 0 && y >= 00 && x <= maxX && y <= maxY
} 
