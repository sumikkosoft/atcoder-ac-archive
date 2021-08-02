package main

import (
	"fmt"
	"math"
)

func main() {
	var (
		a int
	)

	fmt.Scan(&a)

	b := float64(a)
	c := math.Ceil(b / 2.0)

	fmt.Println(int(c))
}
