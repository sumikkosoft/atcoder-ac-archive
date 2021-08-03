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
		x int
	)

	fmt.Scan(&a, &b, &c)
	fmt.Scan(&d)
	tmp := 0

	if b <= d && c >= d {
		tmp += 1
	}

	for i := 1; i < a; i++ {
		fmt.Scan(&x)
		d += x

		if b <= d && c >= d {
			tmp += 1
		}
	}

	fmt.Println(tmp)
}
