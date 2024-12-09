package main

import (
	"fmt"
	"testing"
)

func TestSample(t *testing.T) {
    inputPath := "../input/test.txt"
    expected := 1928
    result := SolvePuzzle(inputPath)

    if (expected != result) {
        t.Fatal(fmt.Printf("Expected %d got %d\n", expected, result))
    }
}

func TestSample2(t *testing.T) {
    inputPath := "../input/test2.txt"
    expected := 1928
    result := SolvePuzzle(inputPath)
    expected = 0*0 + 1*2 + 2*2 + 3*1 + 4*1 + 5*1 + 6*2 + 7*2 + 8*2

    if (expected != result) {
        t.Fatal(fmt.Printf("Expected %d got %d\n", expected, result))
    }
}
