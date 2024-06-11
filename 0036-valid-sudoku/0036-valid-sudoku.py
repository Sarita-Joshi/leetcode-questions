class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        boxes = collections.defaultdict(list)
    
    
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                    
                if cell in rows[i] or cell in cols[j] or cell in boxes[(i//3,j//3)]:
                    return False
                
                rows[i].append(cell) 
                cols[j].append(cell)
                boxes[(i//3,j//3)].append(cell)
                
        return True


                