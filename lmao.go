package main
import ("fmt")

func main() {
	l := [4]string{"a", "b", "c", "d"}
	for i, val := range l {
		fmt.Println(i," ", val)
	}
}