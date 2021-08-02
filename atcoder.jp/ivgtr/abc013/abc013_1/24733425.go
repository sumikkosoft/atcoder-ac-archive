package main

import (
	"fmt"
	"strings"
)

func main() {
	var (
		a string
	)

	alphabet := "ABCDE"

	fmt.Scan(&a)
	x := strings.Index(alphabet, a)
	fmt.Println(x + 1)

}
