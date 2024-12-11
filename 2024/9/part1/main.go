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
	fileQueue := make([]map[string]int, 0)
	currIndex := 0

	for i := 0 ; i < len(data) - 1 ; i += 2 {
		fileId := i
		if fileId > 0 {
			fileId /= 2
		}

		files := data[i]
		freeSpace :=  data[i + 1]

		for range files {
			checkSum += fileId * currIndex
			fmt.Printf("(%d) %d * %d\n", currIndex, fileId, currIndex)
			currIndex += 1
		}

		for range freeSpace {
			if len(fileQueue) == 0 {
				data, fileQueue = moveToQueue(data, fileQueue, i + 1)
				if len(fileQueue) == 0 {
					break
				}
			}
			upNext := fileQueue[0]
			upNext["num"] -= 1
			checkSum += upNext["id"] * currIndex
			fmt.Printf("(%d) %d * %d\n", currIndex, upNext["id"], currIndex)
			currIndex += 1
			
			if upNext["num"] == 0 {
				fileQueue = fileQueue[1:]
			}
		}
	}

	for _, remaining := range fileQueue {
		remaining["num"] -= 1
		checkSum += remaining["id"] * currIndex
		fmt.Printf("(%d) %d * %d\n", currIndex, remaining["id"], currIndex)
		currIndex += 1
			
		if remaining["num"] == 0 {
			fileQueue = fileQueue[1:]
		}
	}

	return checkSum
}

func moveToQueue(data []int, queue []map[string]int, findBeforeIndex int) ([]int, []map[string]int) {
	queueMap := make(map[string]int)
	i := 0
	for ; data[len(data)-1- i] == 0 ; {
		i += 2
	}
	index := len(data)-1- i

	if index <= findBeforeIndex {
		return data, queue
	}

	queueMap["num"] = data[index]
	queueMap["id"] = (index) / 2
	queue = append(queue, queueMap)

	data[len(data)-1 - i] = 0
	return data, queue
}