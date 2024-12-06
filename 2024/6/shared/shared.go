package day6


func GetNewDirection(x int, y int) (int, int){
	if x == -1 {
		return 0, 1
	} else if x == 1 {
		return 0, -1
	} else if y == -1 {
		return -1, 0
	} else {
		return 1, 0
	}
}