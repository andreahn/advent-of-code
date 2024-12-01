package helpers

import (
	"os"
	"strconv"
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