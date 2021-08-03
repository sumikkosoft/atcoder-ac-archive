package main

import (
	"fmt"
	"sort"
)

func main() {
	var (
		a int
		b int
		c int
	)

	fmt.Scan(&a, &b, &c)

	x := []int{a, b, c}
	sort.Sort(sort.IntSlice(x))

	fmt.Println(x[1])
}
