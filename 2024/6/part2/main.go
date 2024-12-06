package main

import (
	"fmt"
	"strings"
	day6 "github.com/andreahn/advent-of-code-2024/6/shared"
	"github.com/andreahn/advent-of-code-2024/helpers"
)

func main() {
	inputPath := "../input/input.txt"
	fmt.Println(SolvePuzzle(inputPath))
	// its friday night and ive been drinking wine so excuse this mess
}

func SolvePuzzle(inputPath string) int {
	startX := 0
	startY := 0

	data := helpers.GetListOfStrings(inputPath)
	for x, v := range data {
		y := strings.Index(v, "^")
		if y > -1 {
			startX = x
			startY = y
			break
		}
	}

	positionsToCheck := getPossiblePositions(data, startX, startY)
	result := 0

	for _, pos := range positionsToCheck {
		x := helpers.StringToInt(strings.Split(pos, ",")[0])
		y := helpers.StringToInt(strings.Split(pos, ",")[1])

		if x == startX && y == startY {
			continue
		}
		
		if checkObstacle(data, startX, startY, x, y) {
			result += 1
		}
	}

	return result
}

func getPossiblePositions(data []string, startX int, startY int) []string {
	visited := make(map[string]bool)

	moveX := -1 // Starts facing up
	moveY := 0
	for ; ; {
		keyInMap := fmt.Sprintf("%d,%d", startX, startY)
		
		visited[keyInMap] = true
		if startX + moveX < 0 || startX + moveX > len(data) - 1 || startY + moveY < 0 || startY + moveY > len(data[0]) - 1 {
			break
		}

		if (string(data[startX + moveX][startY + moveY]) == "#"){
			moveX, moveY = day6.GetNewDirection(moveX, moveY)
		}
		startX += moveX
		startY += moveY
	}
	keys := make([]string, len(visited))

	i := 0
	for k := range visited {
    	keys[i] = k
    	i++
	}

	return keys
}

func checkObstacle(data []string, startX int, startY int, obsX int, obsY int) bool {
	copy := data
	visited := make(map[string]bool)

	moveX := -1 // Starts facing up
	moveY := 0
	for ; ; {
		copy[startX] = copy[startX][:startY] + "X" + copy[startX][startY +1:]
		keyInMap := fmt.Sprintf("%d,%d,%d,%d", startX, startY, moveX, moveY)
		if visited[keyInMap] {
			return true
		}
		
		visited[keyInMap] = true

		nextX := startX + moveX
		nextY := startY + moveY
		if nextX < 0 || nextX > len(data) - 1 || nextY < 0 || nextY > len(data[0]) - 1 {
			return false
		}
		
		for ; (string(data[nextX][nextY]) == "#" || (obsX == nextX && obsY == nextY)) ;{
			moveX, moveY = day6.GetNewDirection(moveX, moveY)
			nextX = startX + moveX
			nextY = startY + moveY
		}
		startX += moveX
		startY += moveY
	}
}
