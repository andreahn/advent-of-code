package main

import (
	"fmt"
	"testing"
)

func Test1(t *testing.T) {
    inputPath := "input/test.txt"
    expected := 2
    result := Part1(inputPath)

    if (expected != result) {
        t.Fatal(fmt.Printf("Expected %d got %d", expected, result))
    }
}
