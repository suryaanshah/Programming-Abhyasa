package main

import (
	"fmt"
)

func main() {
	n := 1 == 1
	m := 1 == 2
	fmt.Printf("%v, %T\n", n, n)
	fmt.Printf("%v, %T", m, m)
}
