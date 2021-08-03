package main

import (
	"fmt"
)

func main() {
	var (
		a int
		b int
		c int
		k int
		s int
		t int
	)

	fmt.Scan(&a, &b, &c, &k)
	fmt.Scan(&s, &t)
	ans := 0

	if s+t >= k {
		a -= c
		b -= c
	}

	ans += a*s + b*t

	fmt.Println(ans)
}
