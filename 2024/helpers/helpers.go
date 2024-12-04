package helpers

import (
	"os"
	"strconv"
	"strings"
)

func ReadInputAsString(inputPath string) string {
	data, err := os.ReadFile(inputPath)
	handleError(err)
	return string(data)
}

func StringToInt(toConvert string) int {
	intValue, err := strconv.Atoi(toConvert)
	handleError(err)
	return intValue
}

func handleError(err error) {
	if err != nil {
		panic(err)
	}
}

func GetIntegerMatrix(inputPath string) [][]int {
	rawData := ReadInputAsString(inputPath)
	data := make([][]int, strings.Count(rawData, "\n")+1)

	splitByLine := strings.Split(rawData, "\n")

	for i, value := range splitByLine {

		for _, v := range strings.Split(value, " ") {
			data[i] = append(data[i], StringToInt(v))
		}
	}

	return data
}

func GetListOfStrings(inputPath string) []string {
	rawData := ReadInputAsString(inputPath)
	rawData = strings.TrimRight(rawData, "\n")
	return strings.Split(rawData, "\n")
}