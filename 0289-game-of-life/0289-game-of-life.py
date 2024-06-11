class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        change_state = []
        inc = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        def get_neighbors(r,c):
            count = 0
            for i,j in inc:
                if 0 <= r+i < m and 0 <= c+j < n and board[r+i][c+j] == 1:
                    count += 1
            return count
            

        for i in range(m):
            for j in range(n):
                neighbors = get_neighbors(i,j)
                if neighbors not in (2,3) and board[i][j]==1:
                    change_state.append((i,j,0))
                elif neighbors==3 and board[i][j]==0:
                    change_state.append((i,j,1))
                    
        for i,j,state in change_state:
            board[i][j] = state
            
            
                
                
                
                
                
        
        