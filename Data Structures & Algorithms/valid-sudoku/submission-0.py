class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        grids = [[] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n=='.': continue
                g = r//3 + (c//3)*3
                
                if n in rows[r]: 
                    return False
                else: rows[r].append(n)

                if n in cols[c]: 
                    return False
                else: cols[c].append(n)

                
                if n in grids[g]: 
                    return False
                else: grids[g].append(n)
                
        return True