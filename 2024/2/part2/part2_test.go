package main

import (
	"fmt"
	"testing"
)

func Test1(t *testing.T) {
    inputPath := "input/test.txt"
    expected := 4
    result := Part2(inputPath)

    if (expected != result) {
        t.Fatal(fmt.Printf("\nExpected %d got %d\n\n", expected, result))
    }
}
