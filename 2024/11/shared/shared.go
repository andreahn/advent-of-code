package day11

import (
	"strconv"

	"github.com/andreahn/advent-of-code-2024/helpers"
)


var cache map[int] map[int]int = make(map[int] map[int]int)

func SolvePuzzle(inputPath string, blinks int) int {
	data := helpers.GetIntegerArray(inputPath, " ")
	total := 0
	for i := 0 ; i < len(data) ; i++ {
		total += solve(data[i], blinks)
	}
	return total
}

func solve(currentNumber int, remainingBlinks int) int {
	res := 0
	if remainingBlinks == 0 {
		return 1
	}

	cachedValue, isInCache := cache[currentNumber]
	if isInCache {
		if cachedValue[remainingBlinks] > 0 {
			return cachedValue[remainingBlinks]
		}
	}
	nextNumbers := make([]int, 0)

	if currentNumber == 0 {
		nextNumbers = append(nextNumbers, 1)
	} else if len(strconv.Itoa(currentNumber)) % 2 == 0 {
		numberAsString := strconv.Itoa(currentNumber)
		index := len(numberAsString)

		if index % 2 == 0 {
			index /= 2
		} else {
			index = index / 2 + 1
		}
		nextNumbers = append(nextNumbers, helpers.StringToInt(numberAsString[:index]))
		nextNumbers = append(nextNumbers, helpers.StringToInt(numberAsString[index:]))
	} else {
		nextNumbers = append(nextNumbers, currentNumber * 2024)
	}

	if cache[currentNumber] == nil {
		cache[currentNumber] = make(map[int]int)
	}

	for _, num := range nextNumbers {
		res += solve(num, remainingBlinks - 1)
	}
	cache[currentNumber][1]  = len(nextNumbers)
	cache[currentNumber][remainingBlinks]  = res
	return res
}
