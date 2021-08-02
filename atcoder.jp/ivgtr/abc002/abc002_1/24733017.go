package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	} else if b > a {
		return b
	} else {
		return a
	}
}

func main() {
	var (
		a int
		b int
	)

	fmt.Scan(&a, &b)

	fmt.Println(max(a, b))
}
