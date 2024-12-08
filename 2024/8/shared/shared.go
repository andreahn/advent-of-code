package day8

func IsInRange (n int, max int) bool {
	return n >= 0 && n < max
}

func GetSignalLocations(data []string) map[string][][]int {
	signalLocations := make(map[string][][]int)

	for x, line := range data {
		for y, char := range line {
			if string(char) != "." {
				signalLocations[string(char)] = append(signalLocations[string(char)], []int{x, y})
			}
		}
	}
	return signalLocations
}