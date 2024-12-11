package main

import (
	"fmt"
	"testing"

	day11 "github.com/andreahn/advent-of-code-2024/11/shared"
)

func TestSample(t *testing.T) {
    inputPath := "../input/test.txt"
    expected := 22
    result := day11.SolvePuzzle(inputPath, 6)

    if (expected != result) {
        t.Fatal(fmt.Printf("Expected %d got %d\n", expected, result))
    }
}

func TestSample2(t *testing.T) {
    inputPath := "../input/test.txt"
    expected := 55312
    result := day11.SolvePuzzle(inputPath, 25)

    if (expected != result) {
        t.Fatal(fmt.Printf("Expected %d got %d\n", expected, result))
    }
}
