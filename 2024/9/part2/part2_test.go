package main

import (
	"fmt"
	"testing"
)

func TestSample(t *testing.T) {
    inputPath := "../input/test.txt"
    expected := 2858
    result := SolvePuzzle(inputPath)

    if (expected != result) {
        t.Fatal(fmt.Printf("Expected %d got %d\n", expected, result))
    }
    
}