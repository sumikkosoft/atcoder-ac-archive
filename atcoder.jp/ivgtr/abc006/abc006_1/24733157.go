package main

import "fmt"

func main() {
	var (
		a int
	)

	fmt.Scan(&a)

	if a%3 == 0 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
