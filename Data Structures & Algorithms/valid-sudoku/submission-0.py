class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set),defaultdict(set),defaultdict(set)
        ROW, COL = len(board), len(board[0])
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == '.':
                    continue
                val = board[r][c]
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3,c // 3)]):
                    return False
            
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3,c // 3)].add(val)
        return True
