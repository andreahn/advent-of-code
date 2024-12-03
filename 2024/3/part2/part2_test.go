package main

import (
	"fmt"
	"testing"
)

func TestSample(t *testing.T) {
    inputPath := "../input/test2.txt"
    expected := 48
    result := SolvePuzzle(inputPath)

    if (expected != result) {
        t.Fatal(fmt.Printf("Expected %d got %d", expected, result))
    }
}