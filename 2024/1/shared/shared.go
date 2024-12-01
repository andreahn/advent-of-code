package day1

import (
	"regexp"

	"github.com/andreahn/advent-of-code-2024/helpers"
)

func GetInputArrays(inputPath string) ([]int, []int){
	data := helpers.ReadInputAsString(inputPath)

	r := regexp.MustCompile(`([0-9]+)   ([0-9]+)\n?`)

	var first []int
	var second []int

	test := r.FindAllStringSubmatch(data, -1)

	for _, value := range test {
		first = append(first, helpers.StringToInt(value[1]))
		second = append(second, helpers.StringToInt(value[2]))
	}

	return first, second
}