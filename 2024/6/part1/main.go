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
}

func SolvePuzzle(inputPath string) int {
	data := helpers.GetListOfStrings(inputPath)
	visited := make(map[string]bool)

	posX := 0
	posY := 0
	for x, v := range data {
		y := strings.Index(v, "^")
		if y > -1 {
			posX = x
			posY = y
		}
	}

	moveX := -1 // Starts facing up
	moveY := 0
	for ; ; {
		visited[fmt.Sprintf("%d,%d", posX, posY)] = true

		if posX + moveX < 0 || posX + moveX > len(data) - 1 || posY + moveY < 0 || posY + moveY > len(data[0]) - 1 {
			break
		}

		if (string(data[posX + moveX][posY + moveY]) == "#"){
			moveX, moveY = day6.GetNewDirection(moveX, moveY)
		}
		posX += moveX
		posY += moveY
	}

	return len(visited)
}
