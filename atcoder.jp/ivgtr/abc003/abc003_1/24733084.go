package main

import "fmt"

func main() {
	var (
		a int
	)

	fmt.Scan(&a)
	a = (a + 1) * 5000

	fmt.Println(a)

}
