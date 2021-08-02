package main

import (
	"fmt"
)

func main() {
	var (
		a int
		b int
	)

	fmt.Scan(&a)
	fmt.Scan(&b)

	if a%b == 0 {
		fmt.Println(0)

	} else {
		x := (a/b + 1) * b

		fmt.Println(x - a)

	}

}
