class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sets = [set() for _ in range(9 + 9 + 9)] # row, column, 3x3 grid
        for i in range(9):
            for j in range(9):
                try: 
                    number = int(board[i][j])
                    if number in sets[i] or number in sets[9 + j] or \
                     number in sets[18 + 3 * (i // 3) + j // 3]:
                        return False
                    else:
                        sets[i].add(number)
                        sets[j + 9].add(number)
                        sets[18 + 3 * (i // 3) + j // 3].add(number)
                except ValueError:
                    pass

        return True