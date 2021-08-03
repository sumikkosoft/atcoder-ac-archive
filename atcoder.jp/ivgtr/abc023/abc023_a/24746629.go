package main

import (
	"fmt"
	"strconv"
)

func main() {
	var (
		a string
	)

	fmt.Scan(&a)
	ans := 0
	for i := 0; i < len(a); i++ {
		tmp := string(a[i])
		x, _ := strconv.Atoi(tmp)
		ans += x
	}

	fmt.Println(ans)
}
