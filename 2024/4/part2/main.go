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
	data := helpers.GetListOfStrings(inputPath)

	result := 0

	for i, line  := range data {
		if i == 0 || i == len(data) - 1 {
			continue
		}
		for j, c := range strings.Split(line, "") {
			if j == 0 || j == len(data) - 1 {
				continue
			}

			if c != "A" {
				continue
			}
			
			topLeft := string(data[i - 1][j - 1])
			topRight := string(data[i - 1][j + 1])
			bottomLeft := string(data[i + 1][j - 1])
			bottomRight := string(data[i + 1][j + 1])

			if (isMAndS(topLeft, bottomRight) && isMAndS(topRight, bottomLeft))  {
				result += 1
			}
		}
	}

	return result
}

func isMAndS(c1 string, c2 string) bool {
	return (c1 == "M" && c2 == "S") || (c1 == "S" && c2 == "M")
}