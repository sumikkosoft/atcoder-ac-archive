package main

import (
	"fmt"
)

func main() {
	var (
		a string
		b string
	)

	fmt.Scan(&a)
	fmt.Scan(&b)

	if len(a) > len(b) {
		fmt.Println(a)

	} else {
		fmt.Println(b)
	}
}
