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
	data := helpers.GetListOfStrings(inputPath)

	totalCount := 0

	// Check horizontal lines
	for _, value  := range data {
		totalCount += checkString(value)
	}

	// Check vertical lines
	totalCount += checkVerticalStrings(data)

	totalCount += checkAllDiagonals(data)

	return totalCount
}


func checkString(stringToCheck string) int {
	r := regexp.MustCompile(`XMAS`)

	test1 := r.FindAllString(stringToCheck, -1)

	r2 := regexp.MustCompile(`SAMX`)
	test2 := r2.FindAllString(stringToCheck, -1)
	return len(test1) + len(test2)
}

func checkVerticalStrings(input []string) int{
	width := len(input[0])
	height := len(input)
	
	result := 0

	for curr_width := 0; curr_width < width; curr_width++ {
		
		verticalString := ""
		for curr_height := 0; curr_height < height; curr_height++ {
			verticalString += string(input[curr_height][curr_width])
		}
		result += checkString(verticalString)
	}
	return result
}

func checkAllDiagonals (input []string) int {
	result := 0

	for startPos := 0; startPos <= len(input); startPos++ {
		diagString1 := ""
		diagString2 := ""
		for i := 0; i < len(input) && startPos + i < len(input); i++ {
			diagString1 += string(input[startPos + i][i])
			diagString2 += string(input[i][startPos + i])
		}

		result += checkString(diagString1)
		if (startPos != 0) {
			result += checkString(diagString2)
		}

		diagString1 = ""
		diagString2 = ""
		posX := startPos
		posY := len(input) - 1
		for i := 0 ; i < len(input) - startPos; i++ {
			diagString1 += string(input[posX + i][posY - i])
			diagString2 += string(input[posX + i - startPos][posY - i - startPos])
		}
		result += checkString(diagString1)
		if (startPos != 0) {
			result += checkString(diagString2)
		}
	}

	return result
}
