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
	r := regexp.MustCompile(`(do)\(\)|(don't)\(\)|mul\((\d{1,3}),(\d{1,3})\)`)

	data := helpers.ReadInputAsString(inputPath)
	matches := r.FindAllStringSubmatch(data, -1)
	result := 0
	activated := true

	for _,value  := range matches {
		if len(value[1]) != 0 {
			// do()
			activated = true
		} else if len(value[2]) != 0 {
			// dont()
			activated = false
		} else if activated {
			result += helpers.StringToInt(value[3]) * helpers.StringToInt(value[4])
		}
	}
	return result
}