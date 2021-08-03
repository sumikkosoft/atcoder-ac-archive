package main

import (
	"fmt"
)

func main() {
	var (
		a int
		b int
		c int
		d int
		e int
		f int
	)

	fmt.Scan(&a, &b)
	fmt.Scan(&c, &d)
	fmt.Scan(&e, &f)

	fmt.Println(a*b/10 + c*d/10 + e*f/10)
}
