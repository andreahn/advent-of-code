package main

import (
	"fmt"
	"testing"
)

func Test1(t *testing.T) {
    inputPath := "input/test1.txt"
    expected := 31
    result := Part2(inputPath)

    if (expected != result) {
        t.Fatal(fmt.Printf("Expected %d got %d", expected, result))
    }
}