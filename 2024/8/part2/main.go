package main

import (
	"fmt"

	day8 "github.com/andreahn/advent-of-code-2024/8/shared"
	"github.com/andreahn/advent-of-code-2024/helpers"
)

func main() {
	inputPath := "../input/input.txt"
	fmt.Println(SolvePuzzle(inputPath))
}

func SolvePuzzle(inputPath string) int {
	data := helpers.GetListOfStrings(inputPath)
	signalLocations := day8.GetSignalLocations(data)
	antinodeLocations := make(map[string]bool)

	for _, signalLocations := range signalLocations {

		for x, signalA := range signalLocations {
			for _, signalB := range signalLocations[x+1:] {

				aX := signalA[0]
				aY := signalA[1]
				bX := signalB[0]
				bY := signalB[1]

				diffX := aX - bX
				diffY := aY - bY

				oneX := aX
				oneY := aY
				for {
					if !(day8.IsInRange(oneX, len(data)) && day8.IsInRange(oneY, len(data[0]))) {
						break
					}
					antinodeLocations[fmt.Sprintf("%d,%d", oneX, oneY)] = true
					oneX += diffX
					oneY += diffY
				}

				twoX := bX
				twoY := bY

				for {
					if !(day8.IsInRange(twoX, len(data)) && day8.IsInRange(twoY, len(data[0]))) {
						break
					}
					antinodeLocations[fmt.Sprintf("%d,%d", twoX, twoY)] = true
					twoX -= diffX
					twoY -= diffY
				}

			}
		}

	}

	return len(antinodeLocations)
}
