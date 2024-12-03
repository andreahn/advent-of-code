package main

import (
	"fmt"
	"regexp"
	"github.com/andreahn/advent-of-code-2024/helpers"
)

func main() {
	inputPath := "../input/input.txt"
	fmt.Println(SolvePuzzle(inputPath))
}

func SolvePuzzle(inputPath string) int {

	r := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)

	data := helpers.ReadInputAsString(inputPath)
	matches := r.FindAllStringSubmatch(data, -1)
	result := 0

	for _,value  := range matches {
		result += helpers.StringToInt(value[1]) * helpers.StringToInt(value[2])
	}
	return result
}