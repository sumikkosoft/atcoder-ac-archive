package main

import "fmt"

func main() {
	var (
		a int
		b int
	)

	fmt.Scan(&a)
	fmt.Scan(&b)

	fmt.Println(a - b)
}
