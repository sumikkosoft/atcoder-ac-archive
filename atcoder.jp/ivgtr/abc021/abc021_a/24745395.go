package main

import (
	"fmt"
)

func main() {
	var (
		a int
	)

	fmt.Scan(&a)

	fmt.Println(a)

	for i := 0; i < a; i++ {
		fmt.Println(1)
	}
}
