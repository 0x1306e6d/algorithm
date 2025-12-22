package leetcode

func isValidSudoku(board [][]byte) bool {
	for y := 0; y < 9; y++ {
		col := make(map[byte]bool)
		for x := 0; x < 9; x++ {
			n := board[y][x]
			if n == '.' {
				continue
			}
			if col[n] {
				return false
			}
			col[n] = true
		}
	}
	for x := 0; x < 9; x++ {
		row := make(map[byte]bool)
		for y := 0; y < 9; y++ {
			n := board[y][x]
			if n == '.' {
				continue
			}
			if row[n] {
				return false
			}
			row[n] = true
		}
	}
	for i := 0; i < 9; i += 3 {
		for j := 0; j < 9; j += 3 {
			sub := make(map[byte]bool)
			for y := 0; y < 3; y++ {
				for x := 0; x < 3; x++ {
					n := board[y+i][x+j]
					if n == '.' {
						continue
					}
					if sub[n] {
						return false
					}
					sub[n] = true
				}
			}
		}
	}
	return true
}
