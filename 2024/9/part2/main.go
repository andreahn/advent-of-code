package main

import (
	"fmt"

	"github.com/andreahn/advent-of-code-2024/helpers"
)

func main() {
	inputPath := "../input/input.txt"
	fmt.Println(SolvePuzzle(inputPath))
}

func SolvePuzzle(inputPath string) int {
	data := helpers.GetIntegerArray(inputPath, "")
	checkSum := 0
	fileQueue := makeQueue(data)
	fileIsUsed := make(map[int]bool)
	currIndex := 0

	for i := 0 ; i < len(data) - 1 ; i += 2 {
		fileId := i
		if fileId > 0 {
			fileId /= 2
		}

		files := data[i]
		freeSpace :=  data[i + 1]

		
		for range files {
			if fileIsUsed[fileId] {
				} else {
					checkSum += fileId * currIndex
				}
				currIndex += 1
			}
		fileIsUsed[fileId] = true
		fileQueue = removeFromQueue(fileId, fileQueue)
		var elementToUse map[string]int
		for ; freeSpace > 0 ; {
			elementToUse, fileQueue = findElementToUseAndRemove(freeSpace, fileQueue)
			fileIsUsed[elementToUse["id"]] = true

			if elementToUse == nil {
				currIndex++
				freeSpace--
			}

			for range elementToUse["num"] {
				checkSum += elementToUse["id"] * currIndex
				currIndex++
				freeSpace--
			}
		}
	}
	return checkSum
}

func makeQueue(data []int) []map[string]int {
	queue := make([]map[string]int, 0)

	for index := 0 ; index < len(data) ; index += 2 {
		elementMap := make(map[string]int)
		elementMap["num"] = data[index]
		elementMap["id"] = (index) / 2

		queue = append(queue, elementMap)
	}
	return queue
}

func removeFromQueue(id int, queue []map[string]int) []map[string]int {
	newQueue := make([]map[string]int, 0)
	for _,val  := range queue {
		if val["id"] == id {
			continue
		}
		newQueue = append(newQueue, val)
	}
	return newQueue
}

func findElementToUseAndRemove(max int, queue []map[string]int) (map[string]int, []map[string]int) {
	index := -1
	for i := len(queue) - 1 ; i >= 0 ; i-- {
		if queue[i]["num"] <= max {
			index = i
			break
		}
	}
	if index >= 0 {
		return queue[index], removeFromQueue(queue[index]["id"], queue)
	}
	return nil, queue
}
