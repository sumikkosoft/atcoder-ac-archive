package main

import (
	"fmt"
)

func main() {
	var (
		a int
	)

	fmt.Scan(&a)
	a++
	if a > 12 {
		fmt.Println(1)

	} else {
		fmt.Println(a)
	}

}
