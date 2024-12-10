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

var cache map[string] map[string] bool = make(map[string] map[string] bool)

func SolvePuzzle(inputPath string) int {
	data := helpers.GetIntegerMatrixNoSpacing(inputPath)
	maxX = len(data) - 1
	maxY = len(data[0]) - 1

	sum := 0

	for x, line := range data {
		for y, val := range line {
			if val == 0 {
				sum += len(findTrailsFromTrailHead(data, x, y))
			}
		}
	}
	return sum
}


func findTrailsFromTrailHead(forestMap [][]int, x int, y int) (map[string] bool){
	currentAltitude := forestMap[x][y]
	key := fmt.Sprintf("%d,%d", x, y)

	cachedValue, isInCache := cache[key]
	if isInCache {
		return cachedValue
	}

	if currentAltitude == 9 {
		newMap := make(map[string] bool)
		newMap[key] = true
		return newMap
	}
	
	reachablePeaks := make(map[string] bool)

	if isInRange(x + 1, y) && forestMap[x + 1][y] == currentAltitude + 1 {
		peaks := findTrailsFromTrailHead(forestMap, x + 1, y)
		for pos := range peaks {
			reachablePeaks[pos] = true
		}
	}

	if isInRange(x - 1, y) && forestMap[x - 1][y] == currentAltitude + 1 {
		peaks := findTrailsFromTrailHead(forestMap, x - 1, y)
		for pos := range peaks {
			reachablePeaks[pos] = true
		}
	}

	if isInRange(x, y + 1) && forestMap[x][y + 1] == currentAltitude + 1 {
		 peaks := findTrailsFromTrailHead(forestMap, x, y + 1)
		for pos := range peaks {
			reachablePeaks[pos] = true
		}
	}

	if isInRange(x, y - 1) && forestMap[x][y - 1] == currentAltitude + 1 {
		peaks := findTrailsFromTrailHead(forestMap, x, y - 1)
		for pos := range peaks {
			reachablePeaks[pos] = true
		}
	}

	cache[key] = reachablePeaks
	return reachablePeaks
}

func isInRange(x int, y int) bool {
	return x >= 0 && y >= 00 && x <= maxX && y <= maxY
} 
