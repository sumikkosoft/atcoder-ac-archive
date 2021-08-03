package main

import (
	"fmt"
	"sort"
)

func findKey(s []int, key int) int {
	for i := 0; i < len(s); i++ {
		if s[i] == key {
			return i
		}
	}
	return -1
}

func main() {
	var (
		a int
		b int
		c int
	)

	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Scan(&c)

	x := []int{a, b, c}
	sort.Sort(sort.Reverse(sort.IntSlice(x)))

	fmt.Println(findKey(x, a) + 1)
	fmt.Println(findKey(x, b) + 1)
	fmt.Println(findKey(x, c) + 1)
}
