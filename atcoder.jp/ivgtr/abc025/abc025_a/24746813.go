package main

import (
	"fmt"
	"os"
)

func main() {
	var (
		s string
		n int
	)

	fmt.Scan(&s)
	fmt.Scan(&n)
	tmp := 0

	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			tmp++
			if tmp == n {
				fmt.Println(s[i:i+1] + s[j:j+1])
				os.Exit(0)
			}

		}

	}

}
